import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    llm_model: str | None = os.getenv("LLM_MODEL", "gpt-4o-mini")


settings = Settings()
