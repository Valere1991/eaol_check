from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class EventType(StrEnum):
    SIGNAL_INGESTED = "eaol.signal.ingested"
    CAUSAL_ANALYSIS_REQUESTED = "eaol.causal_analysis.requested"
    CAUSAL_ANALYSIS_COMPLETED = "eaol.causal_analysis.completed"
    WORKFLOW_STARTED = "eaol.workflow.started"
    LICENSE_CHECKED = "eaol.license.checked"
    NOTIFICATION_REQUESTED = "eaol.notification.requested"
    AUDIT_RECORDED = "eaol.audit.recorded"


class EventEnvelope(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid4()))
    event_type: EventType
    tenant_id: str
    correlation_id: str
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    actor_id: str | None = None
    source_service: str
    payload: dict[str, Any] = Field(default_factory=dict)
    schema_version: str = "1.0"
