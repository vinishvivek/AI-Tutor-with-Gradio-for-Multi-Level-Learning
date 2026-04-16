from openai import OpenAI
from config.settings import settings

class OpenAIClient():
    """Create configured OpenAI client instances for application services."""
    openai_api_key = settings.openai_api_key

    @staticmethod
    def get_openai_api_key() -> OpenAI:
        if not settings.openai_api_key:
            raise ValueError("Missing API key. Add OpenAI API key to .env")

        return OpenAI(api_key=settings.openai_api_key)

