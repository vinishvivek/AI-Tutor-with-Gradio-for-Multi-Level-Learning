from openai import OpenAI

from config.settings import settings


class OpenAIClientFactory:
    """Factory for configured OpenAI client instances."""

    @staticmethod
    def create() -> OpenAI:
        if not settings.openai_api_key:
            raise ValueError("Missing OPENAI_API_KEY in environment.")
        return OpenAI(api_key=settings.openai_api_key)

