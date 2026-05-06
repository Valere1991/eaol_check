from abc import ABC, abstractmethod


class AIProvider(ABC):
    @abstractmethod
    async def complete(self, prompt: str) -> str:
        raise NotImplementedError


class MockAIProvider(AIProvider):
    async def complete(self, prompt: str) -> str:
        return (
            "Synthèse IA locale: les signaux indiquent une corrélation probable entre "
            "hausse des coûts, retard fournisseur et goulot opérationnel."
        )


def get_ai_provider(name: str = "mock") -> AIProvider:
    # Real providers stay behind this boundary: OpenAI/Azure OpenAI/Mistral/self-hosted LLM.
    # The default is mock to keep local tests deterministic and sovereign.
    return MockAIProvider()
