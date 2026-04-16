from ui.gradio_app import GradioTutorApp


def create_app():
    """Create and return the Gradio application instance."""
    return GradioTutorApp().build()
