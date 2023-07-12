from sqlalchemy import Column, Integer, String
from config import Base, engine

class AssessmentSubmission(Base):
    __tablename__ ="assessment_submission"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    question_id = Column(String)
    answer_id = Column(String)

Base.metadata.create_all(engine)