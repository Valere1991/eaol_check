from typing import Any, Literal
from pydantic import BaseModel, Field


SignalType = Literal[
    "transaction",
    "incident",
    "supplier",
    "project",
    "customer",
    "contract",
    "process",
    "document",
    "risk",
    "metric",
]


class EnterpriseSignal(BaseModel):
    type: SignalType
    name: str
    value: Any
    unit: str | None = None
    source: str | None = None
    confidence: float = Field(default=0.7, ge=0, le=1)


class CausalAnalysisRequest(BaseModel):
    tenant_id: str = "demo"
    case_id: str
    question: str
    signals: list[EnterpriseSignal] = Field(default_factory=list)


class EvidenceItem(BaseModel):
    source: str
    entity: str
    relation: str | None = None
    summary: str
    confidence: float = Field(ge=0, le=1)


class ProbableCause(BaseModel):
    title: str
    explanation: str
    confidence: float = Field(ge=0, le=1)
    impacted_entities: list[str] = Field(default_factory=list)
    evidence: list[EvidenceItem] = Field(default_factory=list)


class NextBestAction(BaseModel):
    action: str
    owner_role: str
    workflow_key: str | None = None
    requires_human_approval: bool = True


class CausalAnalysisResponse(BaseModel):
    tenant_id: str
    case_id: str
    answer: str
    probable_causes: list[ProbableCause]
    next_best_actions: list[NextBestAction]
    governance: dict[str, Any]
