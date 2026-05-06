from fastapi import APIRouter, Depends
from pydantic import BaseModel

from apps.api.eaol_api.dependencies import enforce_license
from packages.eaol_core.licensing.models import LicenseFeature
from packages.eaol_core.security.auth import AuthPrincipal, Role, require_roles, require_tenant_access


class WorkflowStartRequest(BaseModel):
    tenant_id: str
    case_id: str
    workflow_key: str = "eaol-root-cause-analysis"
    variables: dict[str, str | int | float | bool] = {}


router = APIRouter(prefix="/api/v1/workflows", tags=["workflows"])


@router.post("/start")
def start_workflow(
    payload: WorkflowStartRequest,
    principal: AuthPrincipal = Depends(require_roles(Role.EAOL_ADMIN, Role.CUSTOMER_ADMIN)),
) -> dict[str, str]:
    require_tenant_access(payload.tenant_id, principal)
    enforce_license(payload.tenant_id, LicenseFeature.CAMUNDA_WORKFLOWS)
    # Boundary for Camunda Zeebe client. Local alpha returns deterministic placeholder.
    return {
        "status": "accepted",
        "workflow_key": payload.workflow_key,
        "case_id": payload.case_id,
        "tenant_id": payload.tenant_id,
        "actor": principal.username,
    }
