# EAOL IT Integrations Guide

## Integration flow

1. EAOL admin creates a customer/tenant.
2. Admin assigns an exact-time license.
3. Admin or customer admin creates integrations.
4. Customer imports data or activates connector sync.
5. EAOL normalizes data into signals, audit records, graph/vector targets.
6. Customer runs causal analysis and Camunda workflow.

## Supported integration types in the pilot

| Type | First functional mode | Real connector target |
|---|---|---|
| Jira | CSV export import | Jira REST API, JQL, OAuth/API token |
| ServiceNow | CSV export import | Table API for incident/change/cmdb_ci |
| Excel | CSV/XLSX manual import | Microsoft Graph workbook API |
| SharePoint | document metadata CSV | Microsoft Graph sites/drives API |
| SAP/ERP | CSV export import | OData/BAPI/IDoc/API Gateway |
| Generic ERP | CSV export import | REST/SFTP/CDC later |

## Jira pilot import

Export Jira issues with columns compatible with `samples/pilot-it/incidents.csv` or map them to:

- `incident_id`
- `tenant_id`
- `opened_at`
- `service_id`
- `service_name`
- `severity`
- `status`
- `title`
- `description`
- `affected_users`
- `downtime_minutes`
- `source_system`

Postman:

```http
POST /api/v1/imports/it/incidents?tenant_id=firma-it
form-data: file=@incidents.csv
```

## ServiceNow pilot import

Use ServiceNow export for incidents/changes and map fields to the same CSV shape. For real connector later:

- endpoint: `/api/now/table/incident`
- endpoint: `/api/now/table/change_request`
- endpoint: `/api/now/table/cmdb_ci`

## Excel / SharePoint

For pilot, export Excel sheets as CSV. Later, use Microsoft Graph:

- `/sites/{site-id}/drives`
- `/drives/{drive-id}/items/{item-id}/workbook`
- document metadata ingestion for evidence traces

## SAP / ERP

For pilot, use extracted CSV from SAP/ERP. Later connector options:

- SAP OData services
- SAP API Business Hub APIs
- IDoc export
- SFTP scheduled extracts
- CDC/replication through enterprise data platform

## Security rules

- Store no secrets in Git.
- Integration config returned by API redacts token/secret/password/key fields.
- Start read-only.
- Every integration creation and import creates audit records.
- No write-back to Jira/ServiceNow/SAP until Camunda approval exists.
