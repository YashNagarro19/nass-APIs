from fastapi import FastAPI
from businnessLogicGetQuestions import GetQuestions as gq

app = FastAPI()

@app.get("/getQuestions")
def getQuestions():
    return gq.businessLogicGetQuetions()

@app.get("/postQuestions")
def getQuestions():
    return gq.businessLogicGetQuetions()

@app.get("/displayResult")
def getQuestions():
    return gq.businessLogicGetQuetions()
