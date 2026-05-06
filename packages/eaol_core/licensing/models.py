from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field


class LicenseTier(StrEnum):
    STARTER = "starter"
    PROFESSIONAL = "professional"
    ENTERPRISE = "enterprise"
    SOVEREIGN = "sovereign"


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


class License(BaseModel):
    license_id: str
    tenant_id: str
    tier: LicenseTier
    starts_on: date
    expires_on: date
    max_users: int
    max_connectors: int
    max_events_per_month: int
    features: set[LicenseFeature] = Field(default_factory=set)


class LicenseCheckResult(BaseModel):
    allowed: bool
    tenant_id: str
    feature: LicenseFeature
    reason: str
    tier: LicenseTier | None = None
