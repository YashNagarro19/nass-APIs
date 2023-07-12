from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from common.getQuestions import GetQuestions
from schemas.generalSchema import Response
from schemas.assessmentSchema import AssessmentQuestionsAnswers
from cruds.assessmentCrud import create_record
import logging

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/getQuestions")
def getQuestions(skip: int = 0, limit: int = 100):
    try:
        return Response(
            code=200,
            status="success",
            result=GetQuestions.getQuestions()
        )
    except Exception as ex:
        logging.error("Exception: "+ str(ex))
        raise HTTPException(status_code=500, detail=str(ex))

@router.post("/postQuestions")
async def postQuestions(request: AssessmentQuestionsAnswers, db: Session = Depends(get_db)):
    print(request)
    for item in request.answerList:
        create_record(db=db, userId=request.userId, questionAnswer=item)
    return Response(
        code=200,
        status="success"
    )