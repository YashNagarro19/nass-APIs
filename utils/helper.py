import json
import logging
from http import HTTPStatus
from collections import defaultdict
from typing import List
from schemas import QuestionAnswer, PlatformReport

answerValueWeightage = {
    "using": 1,
    "want to use": 2,
    "don't want to use": 0,
    "important": 1,
    "very important": 2,
    "not important": 0
}

pillars = ["organization", "security", "governance", "strategy", "cost"]

def readQuestionsFromJSON():
    try:
        with open("common/questionList.json", "r") as json_file:
            stringResponse  = json_file.read()
            response = json.loads(stringResponse)
        return response
    except Exception as ex:
        logging.error("Internal Server Error: " + str(ex))
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR.value
        return response
    
def platformAssessment(answerList: List[QuestionAnswer]):
    threshold = 0
    recommendedPlatform = None
    platformsList = []
    pillarDict = defaultdict(int)
    platformDict = defaultdict(dict)
    for item in answerList:
        answerValue = item.answerValue.lower()
        pillar = item.pillar.lower()
        if pillar in pillars:
            if answerValue in answerValueWeightage:
                pillarDict[pillar]+=answerValueWeightage[answerValue]

    with open("common/platformWeightage.json", "r") as json_file:
        plaformWeightageFile = json_file.read()
        plaformWeightageJSON = json.loads(plaformWeightageFile)

    for platform in plaformWeightageJSON["platforms"]:
        platformDict[platform]["platform"] = platform
        platformDict[platform]["score"] = 0
        for pillar in pillars:
            platformDict[platform][pillar] = int(plaformWeightageJSON["platforms"][platform][pillar]) * int(pillarDict[pillar])
            platformDict[platform]["score"] += int(plaformWeightageJSON["platforms"][platform][pillar]) * int(pillarDict[pillar])  
        
    for platform in platformDict:
        platformsList.append(PlatformReport(**platformDict[platform]))
        if platformDict[platform]["score"] >= threshold:
            recommendedPlatform = platform

    return (recommendedPlatform, platformsList)

    


    
    
    
