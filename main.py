from fastapi import FastAPI
from worker import run_job

app = FastAPI()


@app.get("/")
def root():
    return {"status": "AI Builder Running"}


@app.post("/build")
def build_project(goal: str):
    result = run_job(goal)
    return {"result": result}
