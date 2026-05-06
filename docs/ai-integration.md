# AI Integration Strategy

## Provider boundary

EAOL must support multiple AI providers without changing business logic:

- Mock provider for deterministic local tests
- OpenAI / Azure OpenAI for hosted enterprise deployments
- Mistral or other EU-oriented providers
- Self-hosted LLM for sovereign/on-premise deployments

## Recommended pattern

1. Build a retrieval plan from the user question.
2. Retrieve graph paths and vector context.
3. Build a bounded prompt with only allowed tenant data.
4. Ask the provider for synthesis, not final authority.
5. Validate claims against retrieved evidence.
6. Return confidence, evidence trace, and next-best actions.

## Prompt safety rules

- Never send raw secrets.
- Keep tenant boundary explicit.
- Require answer structure.
- Reject unsupported claims.
- Route actions through Camunda approval.
