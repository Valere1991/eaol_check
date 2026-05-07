# Fix: Keycloak realm `eaol` does not exist

If `http://localhost:8083/realms/eaol` returns 404, your Keycloak container probably started before the realm import file existed. Keycloak does not re-import realm files automatically on every restart.

## Recommended fix

From the backend repo:

```bash
cd /home/ubuntu/.openclaw/workspace/projects/eaol_check
./infra/local/keycloak/apply-eaol-realm.sh
```

Defaults:

```text
KEYCLOAK_URL=http://localhost:8083
KEYCLOAK_ADMIN=admin
KEYCLOAK_ADMIN_PASSWORD=admin
REALM_NAME=eaol
```

## Verify

```bash
curl http://localhost:8083/realms/eaol/.well-known/openid-configuration
```

Expected: JSON OpenID configuration.

## Login users

```text
admin / admin          -> eaol_admin
firma-admin / admin    -> customer_admin
firma-user / admin     -> customer_user
```

## Hard reset local realm

Only for local development:

```bash
RESET_REALM=true ./infra/local/keycloak/apply-eaol-realm.sh
```

This deletes the existing local realm `eaol` and recreates it from `infra/local/keycloak/eaol-realm.json`.
