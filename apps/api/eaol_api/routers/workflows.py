from fastapi import APIRouter
from pydantic import BaseModel


class WorkflowStartRequest(BaseModel):
    tenant_id: str
    case_id: str
    workflow_key: str = "eaol-root-cause-analysis"
    variables: dict[str, str | int | float | bool] = {}


router = APIRouter(prefix="/api/v1/workflows", tags=["workflows"])


@router.post("/start")
def start_workflow(payload: WorkflowStartRequest) -> dict[str, str]:
    # Boundary for Camunda Zeebe client. Local alpha returns deterministic placeholder.
    return {
        "status": "accepted",
        "workflow_key": payload.workflow_key,
        "case_id": payload.case_id,
        "tenant_id": payload.tenant_id,
    }
