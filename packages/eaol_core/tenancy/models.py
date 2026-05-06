from enum import StrEnum

from pydantic import BaseModel, Field


class DeploymentMode(StrEnum):
    SAAS_MULTI_TENANT = "saas_multi_tenant"
    PRIVATE_CLOUD = "private_cloud"
    ON_PREMISE = "on_premise"


class TenantStatus(StrEnum):
    TRIAL = "trial"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    OFFBOARDED = "offboarded"


class Tenant(BaseModel):
    tenant_id: str
    name: str
    sector: str
    deployment_mode: DeploymentMode = DeploymentMode.SAAS_MULTI_TENANT
    status: TenantStatus = TenantStatus.TRIAL
    data_residency_region: str = "EU"
    allowed_ai_providers: list[str] = Field(default_factory=lambda: ["mock"])
