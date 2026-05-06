from enum import StrEnum

from pydantic import BaseModel, EmailStr, Field


class NotificationChannel(StrEnum):
    EMAIL = "email"
    SLACK = "slack"
    TEAMS = "teams"
    WEBHOOK = "webhook"
    IN_APP = "in_app"
    SMS = "sms"


class NotificationSeverity(StrEnum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class NotificationRequest(BaseModel):
    tenant_id: str
    correlation_id: str
    channel: NotificationChannel
    severity: NotificationSeverity = NotificationSeverity.INFO
    subject: str
    message: str
    recipient_email: EmailStr | None = None
    webhook_url: str | None = None
    metadata: dict[str, str] = Field(default_factory=dict)
