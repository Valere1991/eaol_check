# EAOL Enterprise Pilot Security Policy

## Pilot mode constraints

1. Read-only integrations by default.
2. No production writes without Camunda human approval.
3. Use anonymized or minimized data for first pilot.
4. Tenant ID is mandatory for all imported data and audit records.
5. All AI answers must include confidence and evidence trace.
6. Auth starts with Keycloak/OIDC; local dev may run in relaxed mode only.
7. Every import, analysis, workflow start, and notification is auditable.
8. Tokens and secrets must never be committed to Git.

## IT pilot approved data sources

- Jira incidents/changes export
- ServiceNow incidents/changes export
- CMDB asset export
- Datadog/Splunk alerts export

## Prohibited in first pilot

- Customer PII
- Passwords/secrets/API keys
- Financial account data
- Production system mutation
- Fully autonomous remediation
