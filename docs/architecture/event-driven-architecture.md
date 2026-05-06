# Event-Driven Architecture

## Kafka topics

| Topic | Producer | Consumers | Purpose |
|---|---|---|---|
| `eaol.signals` | Ingestion/connectors | Normalization, audit | Raw enterprise signals |
| `eaol.normalized` | Normalization | Graph/vector projectors | Canonical enterprise facts |
| `eaol.causal-analysis` | API/workflows | Reasoning workers | Root-cause requests/results |
| `eaol.workflow-events` | Workflow service | Audit, notification | BPMN lifecycle events |
| `eaol.notifications` | Reasoning/workflow | Notification service | User and system alerts |
| `eaol.audit` | All services | Audit service/SIEM | Immutable trace trail |
| `eaol.license-metering` | API/connectors | License service | Usage and entitlement metering |

## Event envelope

All events use the same envelope:

```json
{
  "event_id": "uuid",
  "event_type": "eaol.signal.ingested",
  "tenant_id": "demo",
  "correlation_id": "case-123",
  "occurred_at": "2026-05-06T16:15:00Z",
  "actor_id": "user-1",
  "source_service": "eaol-api",
  "schema_version": "1.0",
  "payload": {}
}
```

## Design rules

- Every event is tenant-scoped.
- Every causal chain has a `correlation_id`.
- Every AI output and workflow decision emits audit events.
- Event schemas are versioned from day one.
- Kafka is infrastructure; domain logic stays in `packages/eaol_core`.
