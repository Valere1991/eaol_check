from datetime import date, timedelta

import pytest

from packages.eaol_core.licensing.models import License, LicenseFeature, LicenseTier
from packages.eaol_core.licensing.service import LicenseService
from packages.eaol_core.notifications.models import NotificationChannel, NotificationRequest
from packages.eaol_core.notifications.service import NotificationService
from packages.eaol_core.sectors.catalog import SECTOR_PACKS


def test_license_allows_enterprise_feature() -> None:
    license_ = License(
        license_id="lic-1",
        tenant_id="demo",
        tier=LicenseTier.ENTERPRISE,
        starts_on=date.today() - timedelta(days=1),
        expires_on=date.today() + timedelta(days=1),
        max_users=100,
        max_connectors=10,
        max_events_per_month=1000,
        features={LicenseFeature.CAMUNDA_WORKFLOWS},
    )
    result = LicenseService({"demo": license_}).check_feature("demo", LicenseFeature.CAMUNDA_WORKFLOWS)
    assert result.allowed is True


def test_sector_catalog_has_core_industries() -> None:
    assert "finance" in SECTOR_PACKS
    assert "civil_engineering" in SECTOR_PACKS
    assert "mechanical_industry" in SECTOR_PACKS
    assert "it_operations" in SECTOR_PACKS


@pytest.mark.asyncio
async def test_notification_service_queues() -> None:
    service = NotificationService()
    result = await service.send(
        NotificationRequest(
            tenant_id="demo",
            correlation_id="case-1",
            channel=NotificationChannel.IN_APP,
            subject="EAOL alert",
            message="Root cause analysis completed",
        )
    )
    assert result["status"] == "queued"
