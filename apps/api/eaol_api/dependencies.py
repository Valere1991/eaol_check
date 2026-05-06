from datetime import date, timedelta

from packages.eaol_core.licensing.models import License, LicenseFeature, LicenseTier
from packages.eaol_core.licensing.service import LicenseService
from packages.eaol_core.notifications.service import NotificationService


def get_license_service() -> LicenseService:
    demo_license = License(
        license_id="lic-demo-enterprise",
        tenant_id="demo",
        tier=LicenseTier.ENTERPRISE,
        starts_on=date.today() - timedelta(days=1),
        expires_on=date.today() + timedelta(days=365),
        max_users=500,
        max_connectors=25,
        max_events_per_month=1_000_000,
        features={
            LicenseFeature.CAUSAL_INTELLIGENCE,
            LicenseFeature.KNOWLEDGE_GRAPH,
            LicenseFeature.VECTOR_SEARCH,
            LicenseFeature.CAMUNDA_WORKFLOWS,
            LicenseFeature.ADVANCED_CONNECTORS,
            LicenseFeature.SECTOR_PACKS,
            LicenseFeature.SIEM_EXPORT,
        },
    )
    return LicenseService({"demo": demo_license})


def get_notification_service() -> NotificationService:
    return NotificationService()
