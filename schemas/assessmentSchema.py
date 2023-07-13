from typing import Optional, List
from pydantic import BaseModel

class QuestionAnswer(BaseModel):
    questionId: Optional[int]
    answerId: Optional[str]
    answerValue: str
    tag: str
    pillar: str
    detail: Optional[str]

class AssessmentSubmission(BaseModel):
    clientName: Optional[str]
    description: Optional[str]
    geography: Optional[str]
    domain: Optional[str]
    companySize:Optional[int]
    userId: Optional[int]
    answerList: List[QuestionAnswer]

class PlatformReport(BaseModel):
    platform: str
    score: int
    organization: int
    security: int
    governance: int
    strategy: int
    cost: int

class AssessmentSubmissionResponse(BaseModel):
    currentState: Optional[str]
    futureState: Optional[str]
    recommendedPlatform: Optional[str]
    platforms: List[PlatformReport]