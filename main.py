from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/status")
def status():
    return {
        "status": "running",
        "HF_KEY_SET": bool(os.environ.get("HF_API_KEY")),
        "TELEGRAM_KEY_SET": bool(os.environ.get("TELEGRAM_BOT_TOKEN"))
    }

@app.get("/test")
def test():
    return {"message": "Stage 1 safe deployment OK"}
