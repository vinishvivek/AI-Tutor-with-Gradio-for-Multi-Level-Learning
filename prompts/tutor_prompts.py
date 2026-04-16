from app.domain.enums import LearnerLevel
from app.domain.models import TutorRequest


class TutorPromptBuilder:
    """Builds tutoring prompts based on learner level and topic."""

    LEVEL_GUIDANCE = {
        LearnerLevel.BEGINNER: (
            "Explain in simple language, avoid jargon, and use relatable examples."
        ),
        LearnerLevel.INTERMEDIATE: (
            "Explain clearly with moderate technical depth and practical examples."
        ),
        LearnerLevel.ADVANCED: (
            "Provide deeper technical explanation, nuances, and advanced insight."
        ),
    }

    def build_system_prompt(self, request: TutorRequest) -> str:
        guidance = self.LEVEL_GUIDANCE[request.learner_level]
        return (
            "You are an AI tutor helping users learn topics at the right difficulty level. "
            f"{guidance} Keep responses structured, useful, and encouraging."
        )

    def build_user_prompt(self, request: TutorRequest) -> str:
        return (
            f"Topic: {request.topic}\n"
            f"Learner level: {request.learner_level.value}\n"
            f"Question: {request.user_question}\n\n"
            "Respond with:\n"
            "1. A clear explanation\n"
            "2. One practical example\n"
            "3. One suggested follow-up question"
        )