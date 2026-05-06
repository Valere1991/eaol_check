# Firma IT Pilot License

Tenant: `firma-it`
Customer: `Firma IT Pilot GmbH`
Tier: `enterprise`
Validity:

- Starts: `2026-05-06T00:00:00Z`
- Expires: `2026-06-06T23:59:00Z`

When the license is expired, protected EAOL capabilities return HTTP `402 Payment Required` and include the channels where expiration notifications should be queued:

- email
- Teams
- Slack
- webhook
- in-app
- SMS

Protected capabilities:

- causal analysis
- CSV imports
- Camunda workflow start
- dashboard/business features
- notifications

## Check license

```bash
curl http://localhost:8000/api/v1/licenses/firma-it
curl http://localhost:8000/api/v1/licenses/firma-it/features/causal_intelligence
```

## Create a custom exact validity license

```bash
curl -X POST http://localhost:8000/api/v1/licenses \
  -H 'Content-Type: application/json' \
  -d '{
    "tenant_id": "customer-it-prod",
    "customer_name": "Customer IT Production",
    "tier": "enterprise",
    "valid_from": "2026-05-06T22:00:00Z",
    "valid_until": "2026-05-07T22:00:00Z",
    "max_users": 25,
    "max_connectors": 3,
    "max_events_per_month": 10000,
    "features": ["causal_intelligence", "csv_import", "it_pilot", "dashboard", "notifications", "camunda_workflows"],
    "notification_channels": ["email", "teams", "slack", "webhook", "in_app", "sms"]
  }'
```
