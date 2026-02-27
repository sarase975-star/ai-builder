# core/llm_client.py

from openai import OpenAI
import os

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_API_KEY")
)

def call_model(model, messages):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=1500,
    )
    return response.choices[0].message.content
