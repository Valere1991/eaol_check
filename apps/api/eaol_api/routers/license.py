from fastapi import APIRouter, Depends

from apps.api.eaol_api.dependencies import get_license_service
from packages.eaol_core.licensing.models import LicenseCheckResult, LicenseFeature
from packages.eaol_core.licensing.service import LicenseService

router = APIRouter(prefix="/api/v1/licenses", tags=["licenses"])


@router.get("/{tenant_id}/features/{feature}", response_model=LicenseCheckResult)
def check_feature(
    tenant_id: str,
    feature: LicenseFeature,
    service: LicenseService = Depends(get_license_service),
) -> LicenseCheckResult:
    return service.check_feature(tenant_id, feature)
