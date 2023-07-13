from sqlalchemy.orm import Session
from models.assessmentModel import AssessmentSubmission
from schemas.assessmentSchema import QuestionAnswer

def create_record(db: Session, userId: int, questionAnswer: QuestionAnswer):
    _assessmentRecord = AssessmentSubmission(
        user_id=userId, 
        question_id=questionAnswer.questionId, 
        answer_id=questionAnswer.answerId,
        answer_value=questionAnswer.answerValue,
        tag = questionAnswer.tag,
        pillar = questionAnswer.pillar,
        detail = questionAnswer.detail
    )
    db.add(_assessmentRecord)
    db.commit()
    db.refresh(_assessmentRecord)
    return _assessmentRecord