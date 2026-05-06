import json
import sqlite3
from pathlib import Path

from packages.eaol_core.audit.models import AuditRecord


class SQLiteAuditStore:
    def __init__(self, path: str = "data/eaol_audit.db") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

    def _init_schema(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS audit_records (
                    audit_id TEXT PRIMARY KEY,
                    tenant_id TEXT NOT NULL,
                    correlation_id TEXT NOT NULL,
                    actor_id TEXT,
                    action TEXT NOT NULL,
                    resource TEXT NOT NULL,
                    evidence_hash TEXT,
                    metadata_json TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_audit_tenant_created ON audit_records (tenant_id, created_at DESC)"
            )

    def append(self, record: AuditRecord) -> AuditRecord:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO audit_records (
                    audit_id, tenant_id, correlation_id, actor_id, action,
                    resource, evidence_hash, metadata_json, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    record.audit_id,
                    record.tenant_id,
                    record.correlation_id,
                    record.actor_id,
                    record.action,
                    record.resource,
                    record.evidence_hash,
                    json.dumps(record.metadata),
                    record.created_at.isoformat(),
                ),
            )
        return record

    def list_by_tenant(self, tenant_id: str, limit: int = 50) -> list[AuditRecord]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT audit_id, tenant_id, correlation_id, actor_id, action,
                       resource, evidence_hash, metadata_json, created_at
                FROM audit_records
                WHERE tenant_id = ?
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (tenant_id, limit),
            ).fetchall()
        return [
            AuditRecord(
                audit_id=row[0],
                tenant_id=row[1],
                correlation_id=row[2],
                actor_id=row[3],
                action=row[4],
                resource=row[5],
                evidence_hash=row[6],
                metadata=json.loads(row[7]),
                created_at=row[8],
            )
            for row in rows
        ]
