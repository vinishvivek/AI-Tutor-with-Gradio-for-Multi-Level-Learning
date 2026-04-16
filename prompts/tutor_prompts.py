from domain.enums import LearnerLevel
from domain.models import TutorRequest


class TutorPromptBuilder:
    """Builds tutoring prompts based on learner level and topic."""

    LEVEL_GUIDANCE = {
        LearnerLevel.BEGINNER: "Use very simple language and avoid technical jargon.",
        LearnerLevel.INTERMEDIATE: "Use moderate technical depth with practical clarity.",
        LearnerLevel.ADVANCED: "Use deep technical detail, nuances, and advanced reasoning.",
    }

    def build_system_prompt(self, request: TutorRequest) -> str:
        """
        Build the system prompt that defines the tutor's role,
        teaching style, and level-specific explanation depth.
        """
        guidance = self.LEVEL_GUIDANCE[request.learner_level]
        return (
            "You are a helpful, patient AI tutor. "
            "Your job is to teach clearly, use relatable real-world examples, "
            "and explain ideas with analogies whenever useful. "
            f"{guidance}"
        )

    def build_user_prompt(self, request: TutorRequest) -> str:
        """
        Build the user prompt containing the topic, learner level,
        user question, and the required markdown response format.
        """
        return (
            f"Topic: {request.topic}\n"
            f"Learner level: {request.learner_level.value}\n"
            f"Question: {request.user_question}\n\n"
            "Respond in markdown with these sections:\n"
            "## Explanation\n"
            "## Example\n"
            "## Follow-up Question\n\n"
            "Keep the explanation aligned to the learner level."
        )