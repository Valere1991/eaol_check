from fastapi import APIRouter, Depends

from packages.eaol_core.security.auth import AuthPrincipal, get_current_principal

router = APIRouter(prefix="/api/v1/me", tags=["me"])


@router.get("", response_model=AuthPrincipal)
def me(principal: AuthPrincipal = Depends(get_current_principal)) -> AuthPrincipal:
    return principal
