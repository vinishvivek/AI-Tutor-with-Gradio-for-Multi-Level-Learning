import gradio as gr

from app.domain.enums import LearnerLevel
from app.domain.models import TutorRequest
from app.services.tutor_service import TutorService


class GradioTutorApp:
    def __init__(self) -> None:
        self._service = TutorService()

    def _handle_submit(self, topic: str, learner_level: str, user_question: str) -> str:
        request = TutorRequest(
            topic=topic,
            learner_level=LearnerLevel(learner_level),
            user_question=user_question,
        )
        response = self._service.generate_response(request)
        return response.explanation

    def build(self) -> gr.Blocks:
        with gr.Blocks(title="AI Tutor") as demo:
            gr.Markdown("# AI Tutor")
            gr.Markdown("Learn topics at the level that suits you best.")

            topic = gr.Textbox(label="Topic")
            learner_level = gr.Dropdown(
                choices=[level.value for level in LearnerLevel],
                label="Learner Level",
                value=LearnerLevel.BEGINNER.value,
            )
            user_question = gr.Textbox(label="Your Question", lines=6)
            output = gr.Textbox(label="Tutor Response", lines=14)

            submit_btn = gr.Button("Explain")
            submit_btn.click(
                fn=self._handle_submit,
                inputs=[topic, learner_level, user_question],
                outputs=output,
            )

        return demo