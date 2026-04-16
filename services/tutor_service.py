from __future__ import annotations

from collections.abc import Iterator

from clients.openai_client import OpenAIChatGateway
from domain.models import TutorRequest, TutorResponse
from prompts.tutor_prompts import TutorPromptBuilder
from utils.logger import get_logger

logger = get_logger(__name__)


class TutorService:
    """Coordinates prompt generation and model interaction for tutoring responses."""

    def __init__(self) -> None:
        """Initialize the service with the chat gateway and prompt builder."""
        self._gateway = OpenAIChatGateway()
        self._prompt_builder = TutorPromptBuilder()

    def _build_prompts(self, request: TutorRequest) -> tuple[str, str]:
        """
        Build and return the system and user prompts for a tutoring request.

        Args:
            request: The validated tutoring request.

        Returns:
            A tuple containing the system prompt and user prompt.
        """
        system_prompt = self._prompt_builder.build_system_prompt(request)
        user_prompt = self._prompt_builder.build_user_prompt(request)
        return system_prompt, user_prompt

    def stream_response(self, request: TutorRequest) -> Iterator[str]:
        """
        Stream a tutoring response incrementally for display in the UI.

        Args:
            request: The validated tutoring request.

        Yields:
            The progressively accumulated markdown response text.
        """
        try:
            system_prompt, user_prompt = self._build_prompts(request)
            full_result = ""

            for token in self._gateway.stream_chat_completion(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
            ):
                full_result += token
                yield full_result

        except Exception:
            logger.exception("Failed during streamed tutor response.")
            yield "❌ Something went wrong while generating the explanation. Please try again."

    def generate_response(self, request: TutorRequest) -> TutorResponse:
        """
        Generate a complete tutoring response in non-streaming mode.

        Args:
            request: The validated tutoring request.

        Returns:
            A structured TutorResponse containing the final explanation.
        """
        system_prompt, user_prompt = self._build_prompts(request)

        content = self._gateway.complete_chat(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return TutorResponse(
            explanation=content.strip(),
            suggested_follow_up="Would you like a quiz, examples, or a simpler explanation next?",
        )