from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
# from sqlalchemy.orm import Session
# from database import get_db
from utils import readQuestionsFromJSON, platformAssessment
from schemas.generalSchema import Response
from schemas.assessmentSchema import AssessmentSubmission, AssessmentSubmissionResponse
from cruds.assessmentCrud import create_record
import logging

router = APIRouter()

@router.get("/getQuestions")
def getQuestions(skip: int = 0, limit: int = 100):
    try:
        return readQuestionsFromJSON()

    except Exception as ex:
        logging.error("Exception: "+ str(ex))
        raise HTTPException(status_code=500, detail=str(ex))

@router.post("/postQuestions")
async def postQuestions(request: AssessmentSubmission):
    # for item in request.answerList:
    #     create_record(db=db, userId=request.userId, questionAnswer=item)
    recommendedPlatform, platformsList = platformAssessment(answerList=request.answerList)
    
    return AssessmentSubmissionResponse(
        recommendedPlatform=recommendedPlatform,
        platforms=platformsList
    )