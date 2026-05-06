from datetime import UTC, datetime

from packages.eaol_core.licensing.models import License, LicenseFeature, LicenseTier

COMMON_ENTERPRISE_FEATURES = {
    LicenseFeature.CAUSAL_INTELLIGENCE,
    LicenseFeature.KNOWLEDGE_GRAPH,
    LicenseFeature.VECTOR_SEARCH,
    LicenseFeature.CAMUNDA_WORKFLOWS,
    LicenseFeature.ADVANCED_CONNECTORS,
    LicenseFeature.SECTOR_PACKS,
    LicenseFeature.SIEM_EXPORT,
    LicenseFeature.IT_PILOT,
    LicenseFeature.CSV_IMPORT,
    LicenseFeature.DASHBOARD,
    LicenseFeature.NOTIFICATIONS,
}


def seed_licenses() -> dict[str, License]:
    return {
        "demo": License(
            license_id="lic-demo-enterprise",
            tenant_id="demo",
            customer_name="Demo Enterprise",
            tier=LicenseTier.ENTERPRISE,
            valid_from=datetime(2026, 1, 1, 0, 0, tzinfo=UTC),
            valid_until=datetime(2027, 1, 1, 0, 0, tzinfo=UTC),
            max_users=500,
            max_connectors=25,
            max_events_per_month=1_000_000,
            features=COMMON_ENTERPRISE_FEATURES,
        ),
        "firma-it": License(
            license_id="lic-firma-it-pilot-20260506",
            tenant_id="firma-it",
            customer_name="Firma IT Pilot GmbH",
            tier=LicenseTier.ENTERPRISE,
            valid_from=datetime(2026, 5, 6, 0, 0, tzinfo=UTC),
            valid_until=datetime(2026, 6, 6, 23, 59, tzinfo=UTC),
            max_users=75,
            max_connectors=6,
            max_events_per_month=100_000,
            features=COMMON_ENTERPRISE_FEATURES,
            notification_channels=["email", "teams", "slack", "webhook", "in_app", "sms"],
        ),
        "expired-it": License(
            license_id="lic-expired-it-test",
            tenant_id="expired-it",
            customer_name="Expired IT Test Tenant",
            tier=LicenseTier.PROFESSIONAL,
            valid_from=datetime(2026, 1, 1, 0, 0, tzinfo=UTC),
            valid_until=datetime(2026, 1, 2, 0, 0, tzinfo=UTC),
            max_users=10,
            max_connectors=2,
            max_events_per_month=1_000,
            features={LicenseFeature.CAUSAL_INTELLIGENCE, LicenseFeature.CSV_IMPORT},
        ),
    }
