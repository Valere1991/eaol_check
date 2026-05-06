from fastapi import APIRouter

from packages.eaol_core.audit.models import AuditRecord
from packages.eaol_core.audit.store import SQLiteAuditStore

router = APIRouter(prefix="/api/v1/audit", tags=["audit"])


@router.get("/{tenant_id}", response_model=list[AuditRecord])
def list_audit_records(tenant_id: str, limit: int = 50) -> list[AuditRecord]:
    return SQLiteAuditStore().list_by_tenant(tenant_id, limit)
