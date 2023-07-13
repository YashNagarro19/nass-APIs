from fastapi import FastAPI
from routes.assessmentRoute import router
# from database import Base, engine

app = FastAPI()

# Base.metadata.create_all(engine)

app.include_router(router, prefix="/assessment", tags=["assessment"])
