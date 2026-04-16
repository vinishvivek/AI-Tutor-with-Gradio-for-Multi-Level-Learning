from pydantic import BaseModel, Field

from domain.enums import LearnerLevel


class TutorRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=300)
    learner_level: LearnerLevel
    user_question: str = Field(..., min_length=1, max_length=3000)

class TutorResponse(BaseModel):
    explanation: str
    suggested_follow_up: str | None = None