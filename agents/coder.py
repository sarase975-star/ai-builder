# agents/coder.py

from core.llm_client import call_model

def generate_code(step):

    messages = [
        {"role": "system", "content": "You are a senior Python developer. Return full working files."},
        {"role": "user", "content": step}
    ]

    return call_model(
        "moonshotai/Kimi-K2-Instruct-0905:groq",
        messages
    )
