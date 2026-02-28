# agents/debugger.py
import os
from openai import OpenAI

HF_API_KEY = os.environ["HF_API_KEY"]

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_API_KEY,
)

def debug_task(code: str) -> str:
    """
    Fix any issues in code.
    """
    completion = client.chat.completions.create(
        model="moonshotai/Kimi-K2-Instruct-0905",
        messages=[{"role": "user", "content": f"Debug/fix this code:\n{code}"}],
    )
    return completion.choices[0].message
