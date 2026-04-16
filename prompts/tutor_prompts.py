from domain.models import TutorRequest


class TutorPromptBuilder:
    """Builds tutoring prompts based on learner level and topic."""

    LEVEL_GUIDANCE = {
        1: {
            "label": "5 year old",
            "instruction": (
                "Explain as if teaching a very curious 5 year old. "
                "Use extremely simple words, playful analogies, and tiny step-by-step ideas."
            ),
        },
        2: {
            "label": "College student",
            "instruction": (
                "Explain clearly for a college student with basic familiarity. "
                "Use simple practical examples and avoid unnecessary complexity."
            ),
        },
        3: {
            "label": "University student",
            "instruction": (
                "Explain for a university student with solid academic understanding. "
                "Include some technical depth and structured reasoning."
            ),
        },
        4: {
            "label": "PhD graduate",
            "instruction": (
                "Explain with advanced technical depth, precision, and nuanced detail "
                "suitable for a PhD graduate."
            ),
        },
        5: {
            "label": "PhD Einstein Level Mad Scientist",
            "instruction": (
                "Explain with maximum depth, sharp technical rigor, advanced abstractions, "
                "and deep conceptual nuance, while still remaining coherent and teachable."
            ),
        },
    }

    def build_system_prompt(self, request: TutorRequest) -> str:
        """
        Build the system prompt that defines the tutor's role,
        teaching style, and level-specific explanation depth.
        """
        level_info = self.LEVEL_GUIDANCE[request.learner_level]
        return (
            "You are a helpful, patient AI tutor. "
            "Your job is to teach clearly, use relatable real-world examples, "
            "and explain ideas with analogies whenever useful. "
            f"Target explanation level: {level_info['label']}. "
            f"{level_info['instruction']}"
        )

    def build_user_prompt(self, request: TutorRequest) -> str:
        """
        Build the user prompt containing the topic, learner level,
        user question, and required markdown response format.
        """
        level_info = self.LEVEL_GUIDANCE[request.learner_level]
        return (
            f"Topic: {request.topic}\n"
            f"Learner level: {request.learner_level} - {level_info['label']}\n"
            f"Question: {request.user_question}\n\n"
            "Respond in markdown with these sections:\n"
            "## Explanation\n"
            "## Example\n"
            "## Follow-up Question\n\n"
            "Keep the explanation aligned to the learner level."
        )