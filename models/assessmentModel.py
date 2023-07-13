from sqlalchemy import Column, Integer, String
from database import Base

class AssessmentSubmission(Base):
    __tablename__ ="assessment_submission"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    question_id = Column(String)
    answer_id = Column(String)
    answer_value = Column(String)
    tag = Column(String)
    pillar = Column(String)
    detail = Column(String)