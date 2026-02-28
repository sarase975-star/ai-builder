# main.py
import os
from fastapi import FastAPI
from pydantic import BaseModel
from telegram import Bot
from telegram.error import TelegramError

from agents.planner import plan_task
from agents.coder import code_task
from agents.debugger import debug_task

app = FastAPI()

# Telegram bot setup
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if TELEGRAM_BOT_TOKEN:
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
else:
    bot = None

# Simple status endpoint
@app.get("/status")
def status():
    return {"status": "AI Builder Running"}

# Task input model
class TaskRequest(BaseModel):
    prompt: str

# Manual build endpoint
@app.post("/build")
def build_task(task: TaskRequest):
    try:
        # Stage 1 flow: Planner → Coder → Debugger
        plan = plan_task(task.prompt)
        code = code_task(plan)
        fixed_code = debug_task(code)
        return {"plan": plan, "code": code, "fixed_code": fixed_code}
    except Exception as e:
        return {"error": str(e)}

# Optional: Telegram command handler (manual)
@app.post("/telegram_webhook")
def telegram_webhook(update: dict):
    if not bot:
        return {"error": "Telegram bot not configured"}
    try:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        # Call planner → coder → debugger
        plan = plan_task(text)
        code = code_task(plan)
        fixed_code = debug_task(code)
        response = f"Plan:\n{plan}\n\nCode:\n{code}\n\nFixed:\n{fixed_code}"
        bot.send_message(chat_id=chat_id, text=response)
        return {"status": "sent"}
    except TelegramError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}
