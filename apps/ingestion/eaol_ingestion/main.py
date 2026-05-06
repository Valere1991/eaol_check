from packages.eaol_core.events.bus import InMemoryEventBus
from packages.eaol_core.events.models import EventEnvelope, EventType


async def ingest_signal(tenant_id: str, correlation_id: str, payload: dict) -> EventEnvelope:
    event = EventEnvelope(
        event_type=EventType.SIGNAL_INGESTED,
        tenant_id=tenant_id,
        correlation_id=correlation_id,
        source_service="eaol-ingestion",
        payload=payload,
    )
    await InMemoryEventBus().publish("eaol.signals", event)
    return event
