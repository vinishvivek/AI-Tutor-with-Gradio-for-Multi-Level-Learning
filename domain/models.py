from pydantic import BaseModel, Field


class TutorRequest(BaseModel):
    """Represents a validated tutoring request from the user."""

    topic: str = Field(..., min_length=1, max_length=300)
    learner_level: int = Field(..., ge=1, le=5)
    user_question: str = Field(..., min_length=1, max_length=3000)


class TutorResponse(BaseModel):
    """Represents the final non-streaming tutoring response."""

    explanation: str
    suggested_follow_up: str | None = None