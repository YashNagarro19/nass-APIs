import json
import logging
from http import HTTPStatus

class GetQuestions:

    def __init__(self):
       pass
    
    def getQuestions():
        try:
            with open("common/questionList.txt", "r") as json_file:
                stringResponse  = json_file.read()
                response = json.loads(stringResponse)
            return response
        except Exception as ex:
            logging.error("Internal Server Error: " + str(ex))
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR.value
            return response
