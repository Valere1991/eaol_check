from datetime import date

from packages.eaol_core.licensing.models import License, LicenseCheckResult, LicenseFeature


class LicenseService:
    def __init__(self, licenses: dict[str, License] | None = None) -> None:
        self.licenses = licenses or {}

    def check_feature(self, tenant_id: str, feature: LicenseFeature) -> LicenseCheckResult:
        license_ = self.licenses.get(tenant_id)
        if license_ is None:
            return LicenseCheckResult(
                allowed=False,
                tenant_id=tenant_id,
                feature=feature,
                reason="No active license found for tenant.",
            )
        today = date.today()
        if not (license_.starts_on <= today <= license_.expires_on):
            return LicenseCheckResult(
                allowed=False,
                tenant_id=tenant_id,
                feature=feature,
                reason="License is outside validity period.",
                tier=license_.tier,
            )
        if feature not in license_.features:
            return LicenseCheckResult(
                allowed=False,
                tenant_id=tenant_id,
                feature=feature,
                reason="Feature is not included in license tier.",
                tier=license_.tier,
            )
        return LicenseCheckResult(
            allowed=True,
            tenant_id=tenant_id,
            feature=feature,
            reason="Feature allowed.",
            tier=license_.tier,
        )
