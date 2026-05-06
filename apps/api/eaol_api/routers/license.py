from fastapi import APIRouter, Depends

from apps.api.eaol_api.dependencies import get_license_service
from packages.eaol_core.licensing.models import (
    License,
    LicenseCheckResult,
    LicenseCreateRequest,
    LicenseFeature,
)
from packages.eaol_core.licensing.service import LicenseService

router = APIRouter(prefix="/api/v1/licenses", tags=["licenses"])


@router.get("", response_model=list[License])
def list_licenses(service: LicenseService = Depends(get_license_service)) -> list[License]:
    return list(service.licenses.values())


@router.post("", response_model=License)
def create_license(
    payload: LicenseCreateRequest,
    service: LicenseService = Depends(get_license_service),
) -> License:
    return service.create(payload)


@router.get("/{tenant_id}", response_model=License | None)
def get_license(
    tenant_id: str,
    service: LicenseService = Depends(get_license_service),
) -> License | None:
    return service.licenses.get(tenant_id)


@router.get("/{tenant_id}/features/{feature}", response_model=LicenseCheckResult)
def check_feature(
    tenant_id: str,
    feature: LicenseFeature,
    service: LicenseService = Depends(get_license_service),
) -> LicenseCheckResult:
    return service.check_feature(tenant_id, feature)
