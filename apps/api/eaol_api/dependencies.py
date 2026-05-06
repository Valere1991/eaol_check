from fastapi import HTTPException, Request, status

from packages.eaol_core.licensing.catalog import seed_licenses
from packages.eaol_core.licensing.models import LicenseCheckResult, LicenseFeature, LicenseStatus
from packages.eaol_core.licensing.service import LicenseService
from packages.eaol_core.notifications.service import NotificationService

_LICENSE_SERVICE = LicenseService(seed_licenses())


def get_license_service() -> LicenseService:
    return _LICENSE_SERVICE


def get_notification_service() -> NotificationService:
    return NotificationService()


def enforce_license(tenant_id: str, feature: LicenseFeature) -> LicenseCheckResult:
    result = _LICENSE_SERVICE.check_feature(tenant_id, feature)
    if result.allowed:
        return result
    if result.status in {LicenseStatus.EXPIRED, LicenseStatus.MISSING, LicenseStatus.NOT_STARTED}:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail={
                "message": result.reason,
                "tenant_id": tenant_id,
                "feature": feature.value,
                "status": result.status.value,
                "valid_until": result.valid_until.isoformat() if result.valid_until else None,
                "notifications_queued_for_channels": result.notify_channels,
            },
        )
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={
            "message": result.reason,
            "tenant_id": tenant_id,
            "feature": feature.value,
            "status": result.status.value,
        },
    )


async def tenant_from_request(request: Request) -> str:
    if request.method in {"POST", "PUT", "PATCH"}:
        try:
            body = await request.json()
            if isinstance(body, dict) and body.get("tenant_id"):
                return str(body["tenant_id"])
        except Exception:
            pass
    return request.query_params.get("tenant_id") or request.path_params.get("tenant_id") or "demo"
