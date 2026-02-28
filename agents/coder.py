# agents/coder.py
import os
from openai import OpenAI

HF_API_KEY = os.environ["HF_API_KEY"]

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_API_KEY,
)

def code_task(plan: str) -> str:
    """
    Generate code from a plan.
    """
    completion = client.chat.completions.create(
        model="moonshotai/Kimi-K2-Instruct-0905",
        messages=[{"role": "user", "content": f"Write code for this plan:\n{plan}"}],
    )
    return completion.choices[0].message
