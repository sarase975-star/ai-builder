# main.py
from fastapi import FastAPI
import os

# Optional Telegram support
try:
    from telegram import Bot
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    bot = Bot(token=TELEGRAM_BOT_TOKEN) if TELEGRAM_BOT_TOKEN else None
except ImportError:
    bot = None
    TELEGRAM_BOT_TOKEN = None

app = FastAPI()

@app.get("/status")
def status():
    hf_set = bool(os.environ.get("HF_API_KEY"))
    tg_set = bool(TELEGRAM_BOT_TOKEN)
    return {
        "status": "running",
        "HF_KEY_SET": hf_set,
        "TELEGRAM_KEY_SET": tg_set
    }

# Minimal test endpoint for Stage 1
@app.get("/test")
def test():
    # This avoids crashing if agents are missing
    return {"message": "Stage 1 repo OK"}
