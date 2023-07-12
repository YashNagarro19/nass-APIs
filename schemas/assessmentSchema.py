from typing import List
from pydantic import BaseModel

class QuestionAnswer(BaseModel):
    questionId: str
    answerId: str

class AssessmentQuestionsAnswers(BaseModel):
    clientName: str
    description: str
    geography: str
    domain: str
    companySize:int
    userId: int
    answerList: List[QuestionAnswer]

# class AssessmentSubmission(BaseModel):
#     userId: int
#     questionId: str
#     answerId: str

#     class Config:
#         orm_mode = True