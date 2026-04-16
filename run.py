from config.settings import settings
from main import create_app


if __name__ == "__main__":
    app = create_app()
    app.launch(server_name=settings.host, server_port=settings.port)