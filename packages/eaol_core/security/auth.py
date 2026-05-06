import base64
import json
from enum import StrEnum
from typing import Any

from fastapi import Depends, Header, HTTPException, status
from pydantic import BaseModel, Field

from packages.eaol_core.config import settings


class Role(StrEnum):
    EAOL_ADMIN = "eaol_admin"
    CUSTOMER_ADMIN = "customer_admin"
    CUSTOMER_USER = "customer_user"


class AuthPrincipal(BaseModel):
    subject: str
    username: str
    email: str | None = None
    roles: set[str] = Field(default_factory=set)
    tenant_id: str = "demo"
    raw_claims: dict[str, Any] = Field(default_factory=dict)

    def has_role(self, role: Role) -> bool:
        return role.value in self.roles


def get_current_principal(authorization: str | None = Header(default=None)) -> AuthPrincipal:
    if not settings.security_enabled:
        return AuthPrincipal(
            subject="dev-admin",
            username="dev-admin",
            email="admin@eaol.local",
            roles={Role.EAOL_ADMIN.value, Role.CUSTOMER_ADMIN.value, Role.CUSTOMER_USER.value},
            tenant_id=settings.default_tenant_id,
        )

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")

    token = authorization.removeprefix("Bearer ").strip()
    claims = _decode_unverified_jwt(token)
    roles = set(claims.get("realm_access", {}).get("roles", []))
    tenant_id = claims.get("tenant_id") or claims.get("eaol_tenant") or _tenant_from_username(claims.get("preferred_username", ""))
    return AuthPrincipal(
        subject=claims.get("sub", "unknown"),
        username=claims.get("preferred_username", claims.get("email", "unknown")),
        email=claims.get("email"),
        roles=roles,
        tenant_id=tenant_id,
        raw_claims=claims,
    )


def require_roles(*required: Role):
    def dependency(principal: AuthPrincipal = Depends(get_current_principal)) -> AuthPrincipal:
        if principal.has_role(Role.EAOL_ADMIN):
            return principal
        if not any(principal.has_role(role) for role in required):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"message": "Insufficient role", "required_roles": [role.value for role in required]},
            )
        return principal

    return dependency


def require_tenant_access(tenant_id: str, principal: AuthPrincipal) -> None:
    if principal.has_role(Role.EAOL_ADMIN):
        return
    if principal.tenant_id != tenant_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"message": "Tenant access denied", "tenant_id": tenant_id},
        )


def _decode_unverified_jwt(token: str) -> dict[str, Any]:
    try:
        parts = token.split(".")
        if len(parts) < 2:
            raise ValueError("Invalid JWT format")
        payload = parts[1]
        payload += "=" * (-len(payload) % 4)
        return json.loads(base64.urlsafe_b64decode(payload.encode("utf-8")))
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid bearer token") from exc


def _tenant_from_username(username: str) -> str:
    if username.startswith("firma-"):
        return "firma-it"
    return settings.default_tenant_id
