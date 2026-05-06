# Security Architecture

## Security goals

EAOL will sit above critical enterprise systems, so the baseline must be enterprise-grade even in alpha.

## Controls

| Area | Control |
|---|---|
| Identity | OIDC/SAML through Keycloak locally, enterprise IdP later |
| Authorization | RBAC + ABAC, tenant boundary checks, purpose-based access |
| Tenancy | Every API/event/record includes `tenant_id`; cross-tenant denied by default |
| Secrets | `.env` local only, no secrets in Git, managed secrets later |
| AI data policy | Provider allow-list per tenant; no raw secrets sent to LLMs |
| Evidence | Every answer must carry evidence trace and confidence score |
| Actions | No external system action without Camunda human approval |
| Audit | Append-only audit records; SIEM export in Enterprise/Sovereign tiers |
| Encryption | TLS in enterprise; AES-256 at rest via managed DB/storage later |
| Compliance posture | GDPR, ISO 27001, SOC2 readiness, NIS2/DORA where applicable |

## Threat model highlights

- Prompt injection from enterprise documents: mitigate by document isolation, bounded prompts, claim checking.
- Data leakage between tenants: enforce tenant filters at API, event, DB, graph, vector layers.
- Unauthorized automation: all risky actions require Camunda human task approval.
- License abuse: meter users/connectors/events and validate feature entitlements.
- Connector compromise: least-privilege credentials, scoped tokens, rotation, audit.
