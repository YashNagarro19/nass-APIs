from fastapi import FastAPI

app = FastAPI()

@app.get("/userData")
def index():
    return "user details"