from enum import StrEnum

from pydantic import BaseModel


class Action(StrEnum):
    READ_CAUSAL_ANALYSIS = "read:causal-analysis"
    RUN_CAUSAL_ANALYSIS = "run:causal-analysis"
    EXECUTE_WORKFLOW_ACTION = "execute:workflow-action"
    ADMIN_TENANT = "admin:tenant"


class Principal(BaseModel):
    actor_id: str
    tenant_id: str
    roles: set[str]
    attributes: dict[str, str] = {}


class AccessDecision(BaseModel):
    allowed: bool
    reason: str


class AccessPolicy:
    def decide(self, principal: Principal, tenant_id: str, action: Action) -> AccessDecision:
        if principal.tenant_id != tenant_id and "platform_admin" not in principal.roles:
            return AccessDecision(allowed=False, reason="Tenant boundary violation.")
        if (
            action == Action.ADMIN_TENANT
            and "tenant_admin" not in principal.roles
            and "platform_admin" not in principal.roles
        ):
            return AccessDecision(allowed=False, reason="Tenant administration role required.")
        if action == Action.EXECUTE_WORKFLOW_ACTION and "approver" not in principal.roles:
            return AccessDecision(allowed=False, reason="Human approver role required.")
        return AccessDecision(allowed=True, reason="Policy allowed.")
