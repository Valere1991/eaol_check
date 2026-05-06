from pydantic import BaseModel, Field


class ITIncident(BaseModel):
    incident_id: str
    tenant_id: str = "demo"
    opened_at: str
    service_id: str
    service_name: str
    severity: str
    status: str
    title: str
    description: str = ""
    affected_users: int = 0
    downtime_minutes: int = 0
    source_system: str = "csv"


class ITChange(BaseModel):
    change_id: str
    tenant_id: str = "demo"
    implemented_at: str
    service_id: str
    title: str
    risk: str
    status: str
    owner: str
    source_system: str = "csv"


class ITAsset(BaseModel):
    asset_id: str
    tenant_id: str = "demo"
    service_id: str
    asset_type: str
    name: str
    environment: str
    criticality: str
    owner_team: str
    source_system: str = "csv"


class ITAlert(BaseModel):
    alert_id: str
    tenant_id: str = "demo"
    raised_at: str
    service_id: str
    metric: str
    value: str
    threshold: str
    severity: str
    source_system: str = "csv"


class ITImportResult(BaseModel):
    tenant_id: str
    dataset_type: str
    rows_imported: int
    source_filename: str
    correlation_id: str
    normalized_signals: list[dict] = Field(default_factory=list)
