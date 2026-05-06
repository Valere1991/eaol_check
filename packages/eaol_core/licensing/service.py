from datetime import UTC, datetime

from packages.eaol_core.licensing.models import (
    License,
    LicenseCheckResult,
    LicenseCreateRequest,
    LicenseFeature,
    LicenseStatus,
)


class LicenseService:
    def __init__(self, licenses: dict[str, License] | None = None) -> None:
        self.licenses = licenses or {}

    def create(self, request: LicenseCreateRequest) -> License:
        license_ = License(
            license_id=f"lic-{request.tenant_id}-{request.valid_from.strftime('%Y%m%d%H%M%S')}",
            tenant_id=request.tenant_id,
            customer_name=request.customer_name,
            tier=request.tier,
            valid_from=request.valid_from,
            valid_until=request.valid_until,
            max_users=request.max_users,
            max_connectors=request.max_connectors,
            max_events_per_month=request.max_events_per_month,
            features=request.features,
            notification_channels=request.notification_channels,
        )
        self.licenses[request.tenant_id] = license_
        return license_

    def check_feature(self, tenant_id: str, feature: LicenseFeature) -> LicenseCheckResult:
        license_ = self.licenses.get(tenant_id)
        if license_ is None:
            return LicenseCheckResult(
                allowed=False,
                tenant_id=tenant_id,
                feature=feature,
                reason="No active license found for tenant.",
                status=LicenseStatus.MISSING,
                notify_channels=["email", "teams", "slack", "webhook", "in_app", "sms"],
            )
        now = datetime.now(UTC)
        valid_from = _ensure_aware(license_.valid_from)
        valid_until = _ensure_aware(license_.valid_until)
        if now < valid_from:
            return LicenseCheckResult(
                allowed=False,
                tenant_id=tenant_id,
                feature=feature,
                reason="License validity period has not started yet.",
                status=LicenseStatus.NOT_STARTED,
                tier=license_.tier,
                valid_until=license_.valid_until,
                notify_channels=license_.notification_channels,
            )
        if now > valid_until:
            return LicenseCheckResult(
                allowed=False,
                tenant_id=tenant_id,
                feature=feature,
                reason="License has expired. All protected EAOL capabilities are disabled for this tenant.",
                status=LicenseStatus.EXPIRED,
                tier=license_.tier,
                valid_until=license_.valid_until,
                notify_channels=license_.notification_channels,
            )
        if feature not in license_.features:
            return LicenseCheckResult(
                allowed=False,
                tenant_id=tenant_id,
                feature=feature,
                reason="Feature is not included in license tier.",
                status=LicenseStatus.FEATURE_DENIED,
                tier=license_.tier,
                valid_until=license_.valid_until,
                notify_channels=license_.notification_channels,
            )
        return LicenseCheckResult(
            allowed=True,
            tenant_id=tenant_id,
            feature=feature,
            reason="Feature allowed.",
            status=LicenseStatus.ACTIVE,
            tier=license_.tier,
            valid_until=license_.valid_until,
            notify_channels=[],
        )


def _ensure_aware(value: datetime) -> datetime:
    return value.replace(tzinfo=UTC) if value.tzinfo is None else value
