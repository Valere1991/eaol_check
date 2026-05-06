from packages.eaol_core.notifications.models import NotificationRequest


class NotificationService:
    """Notification orchestration boundary.

    Local alpha records notifications in-memory. Production adapters: SMTP, Slack,
    Microsoft Teams, SMS, webhook, in-app websocket/event stream.
    """

    def __init__(self) -> None:
        self.sent: list[NotificationRequest] = []

    async def send(self, notification: NotificationRequest) -> dict[str, str]:
        self.sent.append(notification)
        return {"status": "queued", "channel": notification.channel.value}
