from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AI Tutor"
    environment: str = "development"
    debug: bool = True

    openai_api_key: str
    llm_model: str = "gpt-5.4-mini"
    temperature: float = 0.3
    max_tokens: int = 800

    host: str = "0.0.0.0"
    port: int = 7860

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()