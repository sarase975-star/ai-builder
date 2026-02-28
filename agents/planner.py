# agents/planner.py
import os
from openai import OpenAI

HF_API_KEY = os.environ["HF_API_KEY"]

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_API_KEY,
)

def plan_task(prompt: str) -> str:
    """
    Simple planner: returns plan for the task.
    """
    completion = client.chat.completions.create(
        model="moonshotai/Kimi-K2-Instruct-0905",
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message
