from datetime import UTC, datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class CustomerStatus(StrEnum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    TRIAL = "trial"


class CustomerCreateRequest(BaseModel):
    tenant_id: str
    name: str
    sector: str = "it_operations"
    country: str = "DE"
    admin_email: str
    status: CustomerStatus = CustomerStatus.TRIAL


class Customer(BaseModel):
    tenant_id: str
    name: str
    sector: str
    country: str
    admin_email: str
    status: CustomerStatus
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
