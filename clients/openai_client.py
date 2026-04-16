from __future__ import annotations

from collections.abc import Iterator

from openai import OpenAI

from config.settings import settings


class OpenAIClientFactory:
    """Factory for creating configured OpenAI client instances."""

    @staticmethod
    def create() -> OpenAI:
        """
        Create and return an authenticated OpenAI client.

        Returns:
            A configured OpenAI client instance.

        Raises:
            ValueError: If the OpenAI API key is missing.
        """
        if not settings.openai_api_key:
            raise ValueError("Missing OPENAI_API_KEY in environment.")
        return OpenAI(api_key=settings.openai_api_key)


class OpenAIChatGateway:
    """Gateway for streaming and non-streaming chat completion requests."""

    def __init__(self) -> None:
        """Initialize the gateway with a configured OpenAI client."""
        self._client = OpenAIClientFactory.create()

    def stream_chat_completion(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
    ) -> Iterator[str]:
        """
        Stream chat completion tokens from the model.

        Args:
            system_prompt: The system instruction prompt.
            user_prompt: The user content prompt.

        Yields:
            Incremental text chunks from the streamed response.
        """
        stream = self._client.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=settings.temperature,
            stream=True,
        )

        for chunk in stream:
            delta = chunk.choices[0].delta
            if delta and delta.content:
                yield delta.content

    def complete_chat(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """
        Generate a full chat completion response in a single request.

        Args:
            system_prompt: The system instruction prompt.
            user_prompt: The user content prompt.

        Returns:
            The full generated response text.
        """
        response = self._client.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=settings.temperature,
        )
        return response.choices[0].message.content or ""