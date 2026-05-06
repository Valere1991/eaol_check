# Camunda Local Development

## Local credentials

Current local compose is development-only:

- Zeebe gateway: `localhost:26500`
- Zeebe authentication: disabled via `ZEEBE_BROKER_GATEWAY_SECURITY_AUTHENTICATION_MODE=none`
- Operate: http://localhost:8081
- Tasklist: http://localhost:8082

If Operate/Tasklist ask for credentials, the current compose has no Identity service configured yet. For now, use Zeebe through the EAOL API/workers and consider Operate/Tasklist optional until the Identity profile is added.

## Production target

Production/private-cloud will use Camunda Identity/OIDC integrated with Keycloak or the customer IdP.
