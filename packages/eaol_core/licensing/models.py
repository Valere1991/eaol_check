from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class LicenseTier(StrEnum):
    STARTER = "starter"
    PROFESSIONAL = "professional"
    ENTERPRISE = "enterprise"
    SOVEREIGN = "sovereign"


class LicenseStatus(StrEnum):
    ACTIVE = "active"
    NOT_STARTED = "not_started"
    EXPIRED = "expired"
    MISSING = "missing"
    FEATURE_DENIED = "feature_denied"


class LicenseFeature(StrEnum):
    CAUSAL_INTELLIGENCE = "causal_intelligence"
    KNOWLEDGE_GRAPH = "knowledge_graph"
    VECTOR_SEARCH = "vector_search"
    CAMUNDA_WORKFLOWS = "camunda_workflows"
    ADVANCED_CONNECTORS = "advanced_connectors"
    SECTOR_PACKS = "sector_packs"
    CUSTOM_AI_PROVIDER = "custom_ai_provider"
    ON_PREMISE = "on_premise"
    SIEM_EXPORT = "siem_export"
    WHITE_LABEL = "white_label"
    IT_PILOT = "it_pilot"
    CSV_IMPORT = "csv_import"
    DASHBOARD = "dashboard"
    NOTIFICATIONS = "notifications"


class License(BaseModel):
    license_id: str
    tenant_id: str
    customer_name: str
    tier: LicenseTier
    valid_from: datetime
    valid_until: datetime
    max_users: int
    max_connectors: int
    max_events_per_month: int
    features: set[LicenseFeature] = Field(default_factory=set)
    notification_channels: list[str] = Field(default_factory=lambda: ["email", "teams", "slack", "webhook", "in_app", "sms"])


class LicenseCheckResult(BaseModel):
    allowed: bool
    tenant_id: str
    feature: LicenseFeature
    reason: str
    status: LicenseStatus
    tier: LicenseTier | None = None
    valid_until: datetime | None = None
    notify_channels: list[str] = Field(default_factory=list)


class LicenseCreateRequest(BaseModel):
    tenant_id: str
    customer_name: str
    tier: LicenseTier = LicenseTier.ENTERPRISE
    valid_from: datetime
    valid_until: datetime
    max_users: int = 250
    max_connectors: int = 10
    max_events_per_month: int = 250_000
    features: set[LicenseFeature] = Field(default_factory=set)
    notification_channels: list[str] = Field(default_factory=lambda: ["email", "teams", "slack", "webhook", "in_app", "sms"])
