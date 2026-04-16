from clients.openai_client import OpenAIClientFactory
from config.settings import settings
from domain.models import TutorRequest, TutorResponse
from prompts.tutor_prompts import TutorPromptBuilder


class TutorService:
    """Coordinates tutoring request handling."""

    def __init__(self) -> None:
        self._client = OpenAIClientFactory.create()
        self._prompt_builder = TutorPromptBuilder()

    def generate_response(self, request: TutorRequest) -> TutorResponse:
        system_prompt = self._prompt_builder.build_system_prompt(request)
        user_prompt = self._prompt_builder.build_user_prompt(request)

        response = self._client.chat.completions.create(
            model=settings.llm_model,
            temperature=settings.temperature,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        content = response.choices[0].message.content or ""
        return TutorResponse(
            explanation=content.strip(),
            suggested_follow_up="Would you like a quiz or a simpler explanation next?",
        )