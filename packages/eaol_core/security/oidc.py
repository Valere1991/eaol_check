from pydantic import BaseModel


class OIDCConfig(BaseModel):
    issuer: str
    audience: str = "eaol-api"
    jwks_url: str
    mode: str = "dev"


def keycloak_local_config(base_url: str = "http://localhost:8083", realm: str = "eaol") -> OIDCConfig:
    issuer = f"{base_url}/realms/{realm}"
    return OIDCConfig(
        issuer=issuer,
        jwks_url=f"{issuer}/protocol/openid-connect/certs",
    )
