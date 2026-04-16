from ui.gradio_app import GradioTutorApp


def create_app():
    return GradioTutorApp().build()