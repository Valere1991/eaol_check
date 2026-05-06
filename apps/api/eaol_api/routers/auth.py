from fastapi import APIRouter

from packages.eaol_core.security.oidc import OIDCConfig, keycloak_local_config

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@router.get("/oidc-local", response_model=OIDCConfig)
def oidc_local_config() -> OIDCConfig:
    return keycloak_local_config()
