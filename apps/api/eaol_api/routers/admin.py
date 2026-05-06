from fastapi import APIRouter

from packages.eaol_core.audit.models import AuditRecord
from packages.eaol_core.audit.store import SQLiteAuditStore
from packages.eaol_core.customers.models import Customer, CustomerCreateRequest
from packages.eaol_core.integrations.models import Integration, IntegrationCreateRequest
from packages.eaol_core.licensing.models import License, LicenseCreateRequest
from packages.eaol_core.platform.store import PlatformStore

router = APIRouter(prefix="/api/v1/admin", tags=["admin"])


@router.post("/customers", response_model=Customer)
def create_customer(payload: CustomerCreateRequest) -> Customer:
    customer = PlatformStore().create_customer(payload)
    SQLiteAuditStore().append(
        AuditRecord(
            tenant_id=customer.tenant_id,
            correlation_id=f"customer-{customer.tenant_id}",
            action="customer_created",
            resource=f"customer/{customer.tenant_id}",
            metadata=customer.model_dump(mode="json"),
        )
    )
    return customer


@router.get("/customers", response_model=list[Customer])
def list_customers() -> list[Customer]:
    return PlatformStore().list_customers()


@router.post("/customers/{tenant_id}/license", response_model=License)
def assign_license(tenant_id: str, payload: LicenseCreateRequest) -> License:
    normalized = payload.model_copy(update={"tenant_id": tenant_id})
    license_ = PlatformStore().save_license(normalized)
    SQLiteAuditStore().append(
        AuditRecord(
            tenant_id=tenant_id,
            correlation_id=f"license-{license_.license_id}",
            action="license_assigned",
            resource=f"license/{license_.license_id}",
            metadata=license_.model_dump(mode="json"),
        )
    )
    return license_


@router.get("/licenses", response_model=list[License])
def list_platform_licenses() -> list[License]:
    return PlatformStore().list_licenses()


@router.post("/integrations", response_model=Integration)
def create_integration(payload: IntegrationCreateRequest) -> Integration:
    integration = PlatformStore().create_integration(payload)
    SQLiteAuditStore().append(
        AuditRecord(
            tenant_id=integration.tenant_id,
            correlation_id=f"integration-{integration.integration_id}",
            action="integration_created",
            resource=f"integration/{integration.integration_id}",
            metadata=integration.model_dump(mode="json"),
        )
    )
    return integration


@router.get("/integrations/{tenant_id}", response_model=list[Integration])
def list_integrations(tenant_id: str) -> list[Integration]:
    return PlatformStore().list_integrations(tenant_id)
