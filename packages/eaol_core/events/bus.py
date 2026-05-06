from abc import ABC, abstractmethod

from packages.eaol_core.events.models import EventEnvelope


class EventBus(ABC):
    @abstractmethod
    async def publish(self, topic: str, event: EventEnvelope) -> None:
        raise NotImplementedError


class InMemoryEventBus(EventBus):
    def __init__(self) -> None:
        self.events: list[tuple[str, EventEnvelope]] = []

    async def publish(self, topic: str, event: EventEnvelope) -> None:
        self.events.append((topic, event))


class KafkaEventBus(EventBus):
    """Kafka/Redpanda adapter boundary.

    Keep the alpha dependency-light. Production can wire aiokafka/confluent-kafka here.
    """

    def __init__(self, bootstrap_servers: str) -> None:
        self.bootstrap_servers = bootstrap_servers

    async def publish(self, topic: str, event: EventEnvelope) -> None:
        raise NotImplementedError("Kafka adapter is defined as a production boundary for now.")
