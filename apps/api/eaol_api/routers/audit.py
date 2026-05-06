from fastapi import APIRouter, Depends

from packages.eaol_core.audit.models import AuditRecord
from packages.eaol_core.audit.store import SQLiteAuditStore
from packages.eaol_core.security.auth import AuthPrincipal, Role, require_roles, require_tenant_access

router = APIRouter(prefix="/api/v1/audit", tags=["audit"])


@router.get("/{tenant_id}", response_model=list[AuditRecord])
def list_audit_records(
    tenant_id: str,
    limit: int = 50,
    principal: AuthPrincipal = Depends(require_roles(Role.EAOL_ADMIN, Role.CUSTOMER_ADMIN, Role.CUSTOMER_USER)),
) -> list[AuditRecord]:
    require_tenant_access(tenant_id, principal)
    return SQLiteAuditStore().list_by_tenant(tenant_id, limit)
