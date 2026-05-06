from fastapi import APIRouter, Depends

from apps.api.eaol_api.dependencies import get_notification_service
from packages.eaol_core.notifications.models import NotificationRequest
from packages.eaol_core.notifications.service import NotificationService

router = APIRouter(prefix="/api/v1/notifications", tags=["notifications"])


@router.post("")
async def send_notification(
    payload: NotificationRequest,
    service: NotificationService = Depends(get_notification_service),
) -> dict[str, str]:
    return await service.send(payload)
