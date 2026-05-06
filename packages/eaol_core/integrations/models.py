from datetime import UTC, datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class IntegrationType(StrEnum):
    JIRA = "jira"
    SERVICENOW = "servicenow"
    EXCEL = "excel"
    SHAREPOINT = "sharepoint"
    SAP = "sap"
    ERP = "erp"
    CSV = "csv"


class IntegrationStatus(StrEnum):
    DRAFT = "draft"
    ACTIVE = "active"
    DISABLED = "disabled"
    ERROR = "error"


class IntegrationCreateRequest(BaseModel):
    tenant_id: str
    integration_type: IntegrationType
    name: str
    base_url: str | None = None
    auth_mode: str = "api_token"
    scopes: list[str] = Field(default_factory=list)
    config: dict[str, str] = Field(default_factory=dict)


class Integration(BaseModel):
    integration_id: str
    tenant_id: str
    integration_type: IntegrationType
    name: str
    base_url: str | None = None
    auth_mode: str
    scopes: list[str] = Field(default_factory=list)
    config: dict[str, str] = Field(default_factory=dict)
    status: IntegrationStatus = IntegrationStatus.DRAFT
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
