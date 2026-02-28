# main.py
from fastapi import FastAPI
import os

app = FastAPI()

# Telegram lazy-init
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = None
def get_bot():
    global bot
    if bot is None and TELEGRAM_BOT_TOKEN:
        try:
            from telegram import Bot
            bot = Bot(token=TELEGRAM_BOT_TOKEN)
        except ImportError:
            bot = None
    return bot

@app.get("/status")
def status():
    hf_set = bool(os.environ.get("HF_API_KEY"))
    tg_set = bool(TELEGRAM_BOT_TOKEN)
    return {
        "status": "running",
        "HF_KEY_SET": hf_set,
        "TELEGRAM_KEY_SET": tg_set
    }

@app.get("/test")
def test():
    """
    Simple test endpoint.
    """
    return {"message": "Stage 1 safe deployment OK"}
