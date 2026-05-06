# Camunda Local Development

## Local credentials requested for browser access

Use the local proxy:

- Camunda proxy: http://localhost:8090
- Operate through proxy: http://localhost:8090/operate/
- Tasklist through proxy: http://localhost:8090/tasklist/
- Username: `admin`
- Password: `admin`

This is an Nginx basic-auth proxy for local development only.

## Zeebe

- Zeebe gateway: `localhost:26500`
- Zeebe authentication: disabled via `ZEEBE_BROKER_GATEWAY_SECURITY_AUTHENTICATION_MODE=none`

## Direct Camunda apps

- Direct Operate: http://localhost:8081
- Direct Tasklist: http://localhost:8082

If the direct apps require Camunda Identity in your image/version, use the proxy for the browser test and the Zeebe gateway for workers/API. Production/private-cloud will use Camunda Identity/OIDC integrated with Keycloak or the customer IdP.
