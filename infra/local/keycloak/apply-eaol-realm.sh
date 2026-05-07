#!/usr/bin/env bash
set -euo pipefail

KEYCLOAK_URL="${KEYCLOAK_URL:-http://localhost:8083}"
KEYCLOAK_ADMIN="${KEYCLOAK_ADMIN:-admin}"
KEYCLOAK_ADMIN_PASSWORD="${KEYCLOAK_ADMIN_PASSWORD:-admin}"
REALM_FILE="${REALM_FILE:-$(dirname "$0")/eaol-realm.json}"
REALM_NAME="${REALM_NAME:-eaol}"
RESET_REALM="${RESET_REALM:-false}"

if [ ! -f "$REALM_FILE" ]; then
  echo "Realm file not found: $REALM_FILE" >&2
  exit 1
fi

echo "Waiting for Keycloak at $KEYCLOAK_URL ..."
for _ in $(seq 1 60); do
  if curl -fsS "$KEYCLOAK_URL/realms/master" >/dev/null 2>&1; then
    break
  fi
  sleep 2
done

TOKEN="$(
  curl -fsS -X POST "$KEYCLOAK_URL/realms/master/protocol/openid-connect/token" \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'client_id=admin-cli' \
    -d 'grant_type=password' \
    -d "username=$KEYCLOAK_ADMIN" \
    -d "password=$KEYCLOAK_ADMIN_PASSWORD" \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["access_token"])'
)"

realm_exists() {
  curl -fsS -o /dev/null -w '%{http_code}' \
    -H "Authorization: Bearer $TOKEN" \
    "$KEYCLOAK_URL/admin/realms/$REALM_NAME"
}

STATUS="$(realm_exists || true)"

if [ "$STATUS" = "200" ] && [ "$RESET_REALM" = "true" ]; then
  echo "Deleting existing realm $REALM_NAME because RESET_REALM=true ..."
  curl -fsS -X DELETE \
    -H "Authorization: Bearer $TOKEN" \
    "$KEYCLOAK_URL/admin/realms/$REALM_NAME"
  STATUS="404"
fi

if [ "$STATUS" != "200" ]; then
  echo "Creating realm $REALM_NAME from $REALM_FILE ..."
  curl -fsS -X POST "$KEYCLOAK_URL/admin/realms" \
    -H "Authorization: Bearer $TOKEN" \
    -H 'Content-Type: application/json' \
    --data-binary "@$REALM_FILE"
else
  echo "Realm $REALM_NAME already exists. Updating roles, clients and users with partial import ..."
  TMP_IMPORT="$(mktemp)"
  python3 - "$REALM_FILE" > "$TMP_IMPORT" <<'PY'
import json, sys
src = json.load(open(sys.argv[1]))
payload = {
    "ifResourceExists": "OVERWRITE",
    "roles": src.get("roles", {}),
    "clients": src.get("clients", []),
    "users": src.get("users", []),
}
print(json.dumps(payload))
PY
  curl -fsS -X POST "$KEYCLOAK_URL/admin/realms/$REALM_NAME/partialImport" \
    -H "Authorization: Bearer $TOKEN" \
    -H 'Content-Type: application/json' \
    --data-binary "@$TMP_IMPORT" >/dev/null
  rm -f "$TMP_IMPORT"
fi

echo "Verifying realm $REALM_NAME ..."
curl -fsS "$KEYCLOAK_URL/realms/$REALM_NAME/.well-known/openid-configuration" >/dev/null

echo "OK: realm $REALM_NAME is available."
echo "Keycloak: $KEYCLOAK_URL"
echo "Users: admin/admin, firma-admin/admin, firma-user/admin"
