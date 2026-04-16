from __future__ import annotations

from collections.abc import Iterator

import gradio as gr
from pydantic import ValidationError

from domain.models import TutorRequest
from services.tutor_service import TutorService


class GradioTutorApp:
    """Build and manage the Gradio user interface for the AI Tutor."""

    def __init__(self) -> None:
        """Initialize the UI with the tutoring service."""
        self._service = TutorService()

    def _handle_submit(
            self,
            topic: str,
            learner_level: int,
            user_question: str,
    ) -> Iterator[str]:
        """
        Validate user input and stream the tutoring response.

        Args:
            topic: The learning topic entered by the user.
            learner_level: The selected explanation level from 1 to 5.
            user_question: The user's question.

        Yields:
            Incrementally updated markdown response text.
        """
        topic = topic.strip()
        user_question = user_question.strip()

        if not topic and not user_question:
            yield "Please enter both a topic and a question."
            return

        if not topic:
            yield "Please enter a topic before submitting."
            return

        if not user_question:
            yield "Please enter a question before submitting."
            return

        try:
            request = TutorRequest(
                topic=topic,
                learner_level=int(learner_level),
                user_question=user_question,
            )
        except ValidationError:
            yield (
                "Your input is invalid. Please keep the topic under 300 characters, "
                "the question under 3000 characters, and the level between 1 and 5."
            )
            return

        yield from self._service.stream_response(request)

    def build(self) -> gr.Blocks:
        """
        Build and return the Gradio Blocks interface.

        Returns:
            A configured Gradio Blocks application.
        """
        with gr.Blocks(title="AI Tutor") as demo:
            gr.Markdown("# AI Tutor")
            gr.Markdown("Learn any topic at the level that suits you best.")

            topic = gr.Textbox(label="Topic", placeholder="e.g. Neural Networks", container=True)

            gr.Markdown(
                """
            **Levels**
            - **1** — 5 year old  
            - **2** — College student  
            - **3** — University student  
            - **4** — PhD graduate  
            - **5** — PhD Einstein-Level Mad Scientist
            """
            )

            learner_level = gr.Slider(
                minimum=1,
                maximum=5,
                step=1,
                value=2,
                label="Explanation Level",
            )

            user_question = gr.Textbox(
                label="Your Question",
                lines=5,
                placeholder="Ask your question here...",
            )

            output = gr.Markdown(label="Tutor Response")

            submit_button = gr.Button("Explain")
            submit_button.click(
                fn=self._handle_submit,
                inputs=[topic, learner_level, user_question],
                outputs=output,
            )

        return demo