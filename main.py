from fastapi import FastAPI
from businessLogicGetQuestions import GetQuestions as gq
from http import HTTPStatus
import asyncio
import logging

app = FastAPI()

@app.get("/getQuestions", status_code=HTTPStatus.OK.value )
def getQuestions():
    try:
        response = gq.getQuestion()
        return response
    except Exception as ex:
         logging.error("main file exception"+ str(ex))
         print("main exception" + str(ex))
         __json_date = str({})
         raise Exception(HTTPStatus.BAD_REQUEST.value)

@app.get("/postQuestions")
def getQuestions():
    return gq.businessLogicGetQuetions()

@app.get("/displayResult")
def getQuestions():
    return gq.businessLogicGetQuetions()
