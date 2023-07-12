from fastapi import FastAPI
from routes.assessmentRoute import router

app = FastAPI()

app.include_router(router, prefix="/assessment", tags=["assessment"])
