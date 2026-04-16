from config.settings import settings
from main import create_app


def main() -> None:
    """Launch the AI Tutor Gradio application."""
    app = create_app()
    app.launch()


if __name__ == "__main__":
    main()
