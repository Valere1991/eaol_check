import sqlite3
from pathlib import Path
from uuid import uuid4

from packages.eaol_core.customers.models import Customer, CustomerCreateRequest
from packages.eaol_core.integrations.models import Integration, IntegrationCreateRequest, IntegrationStatus
from packages.eaol_core.licensing.models import License, LicenseCreateRequest
from packages.eaol_core.licensing.service import LicenseService


class PlatformStore:
    def __init__(self, path: str = "data/eaol_platform.db") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS customers (
                  tenant_id TEXT PRIMARY KEY,
                  name TEXT NOT NULL,
                  sector TEXT NOT NULL,
                  country TEXT NOT NULL,
                  admin_email TEXT NOT NULL,
                  status TEXT NOT NULL,
                  created_at TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS licenses (
                  tenant_id TEXT PRIMARY KEY,
                  license_json TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS integrations (
                  integration_id TEXT PRIMARY KEY,
                  tenant_id TEXT NOT NULL,
                  integration_json TEXT NOT NULL
                )
                """
            )

    def create_customer(self, request: CustomerCreateRequest) -> Customer:
        customer = Customer(**request.model_dump())
        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO customers
                (tenant_id, name, sector, country, admin_email, status, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    customer.tenant_id,
                    customer.name,
                    customer.sector,
                    customer.country,
                    customer.admin_email,
                    customer.status.value,
                    customer.created_at.isoformat(),
                ),
            )
        return customer

    def list_customers(self) -> list[Customer]:
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM customers ORDER BY created_at DESC").fetchall()
        return [Customer(**dict(row)) for row in rows]

    def save_license(self, request: LicenseCreateRequest) -> License:
        license_ = LicenseService().create(request)
        with self._connect() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO licenses (tenant_id, license_json) VALUES (?, ?)",
                (license_.tenant_id, license_.model_dump_json()),
            )
        return license_

    def list_licenses(self) -> list[License]:
        with self._connect() as conn:
            rows = conn.execute("SELECT license_json FROM licenses").fetchall()
        return [License.model_validate_json(row["license_json"]) for row in rows]

    def create_integration(self, request: IntegrationCreateRequest) -> Integration:
        integration = Integration(
            integration_id=f"int-{request.integration_type.value}-{uuid4()}",
            tenant_id=request.tenant_id,
            integration_type=request.integration_type,
            name=request.name,
            base_url=request.base_url,
            auth_mode=request.auth_mode,
            scopes=request.scopes,
            config=_redact_config(request.config),
            status=IntegrationStatus.ACTIVE,
        )
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO integrations (integration_id, tenant_id, integration_json) VALUES (?, ?, ?)",
                (integration.integration_id, integration.tenant_id, integration.model_dump_json()),
            )
        return integration

    def list_integrations(self, tenant_id: str) -> list[Integration]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT integration_json FROM integrations WHERE tenant_id = ? ORDER BY integration_id DESC",
                (tenant_id,),
            ).fetchall()
        return [Integration.model_validate_json(row["integration_json"]) for row in rows]


def _redact_config(config: dict[str, str]) -> dict[str, str]:
    redacted = {}
    for key, value in config.items():
        if any(secret in key.lower() for secret in ["token", "secret", "password", "key"]):
            redacted[key] = "***redacted***" if value else ""
        else:
            redacted[key] = value
    return redacted
