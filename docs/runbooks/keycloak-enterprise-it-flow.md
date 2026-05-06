# EAOL Keycloak Enterprise IT Flow

## Goal

Run EAOL in a realistic IT enterprise pilot where:

- EAOL platform admin logs into the dashboard.
- Admin creates a customer and assigns an exact-time license.
- Customer admin logs in and configures integrations.
- Customer user runs IT analysis and reads audit.
- Backend endpoints enforce Keycloak realm roles.

## Keycloak realm

Realm file:

```text
infra/local/keycloak/eaol-realm.json
```

It imports realm `eaol`, client `eaol-dashboard`, and users:

| User | Password | Role | Purpose |
|---|---|---|---|
| `admin` | `admin` | `eaol_admin` | EAOL platform admin |
| `firma-admin` | `admin` | `customer_admin` | Customer IT admin |
| `firma-user` | `admin` | `customer_user` | Customer analyst/user |

## Start local stack

```bash
cd infra/local
docker compose -f docker-compose.example.yml up -d keycloak postgres neo4j redpanda zeebe operate tasklist camunda-proxy redis minio mailhog
```

Keycloak:

```text
http://localhost:8083
admin / admin
```

Dashboard client:

```text
realm: eaol
client: eaol-dashboard
redirect: http://localhost:4200/*
```

## Backend security mode

Default local mode is relaxed:

```env
EAOL_SECURITY_ENABLED=false
```

To enforce Keycloak bearer tokens:

```env
EAOL_SECURITY_ENABLED=true
EAOL_KEYCLOAK_ISSUER=http://localhost:8083/realms/eaol
EAOL_KEYCLOAK_CLIENT_ID=eaol-dashboard
```

Then restart FastAPI.

## Role enforcement

| Endpoint group | Roles |
|---|---|
| Create/list customers | `eaol_admin` |
| Assign/list platform licenses | `eaol_admin` |
| Create integrations | `eaol_admin`, `customer_admin` |
| List integrations | `eaol_admin`, `customer_admin`, `customer_user` |
| Import IT CSV | `eaol_admin`, `customer_admin` |
| Start workflows | `eaol_admin`, `customer_admin` |
| Run causal analysis | `eaol_admin`, `customer_admin`, `customer_user` |
| Read tenant audit | `eaol_admin`, `customer_admin`, `customer_user` |

Tenant isolation:

- `eaol_admin` can access all tenants.
- `firma-admin` and `firma-user` are mapped to tenant `firma-it` in local pilot.
- Non-admin users cannot access other tenants.

## Frontend

```bash
cd /home/ubuntu/.openclaw/workspace/projects/eaol_check_fe
npm install --include=dev
npm start
```

Open:

```text
http://localhost:4200
```

Click **Login** and choose one of the Keycloak users.

## Functional pilot sequence

1. Login as `admin/admin`.
2. Create customer `firma-it`.
3. Assign license to `firma-it`.
4. Create Jira/ServiceNow/SAP/Excel/SharePoint integration placeholder.
5. Logout, login as `firma-admin/admin`.
6. List/create integrations for `firma-it`.
7. Import IT CSV via Postman/API.
8. Logout, login as `firma-user/admin`.
9. Run German causal analysis.
10. Read audit.

## Integration documentation

See:

```text
docs/integrations/it-integrations.md
```
