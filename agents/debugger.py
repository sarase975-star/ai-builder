# agents/debugger.py

from core.llm_client import call_model

def fix_code(code, error):

    messages = [
        {"role": "system", "content": "You are an expert debugger. Fix the code fully."},
        {"role": "user", "content": f"Code:\n{code}\n\nError:\n{error}"}
    ]

    return call_model(
        "moonshotai/Kimi-K2-Instruct-0905:groq",
        messages
    )
