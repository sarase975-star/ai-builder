# agents/coder.py
import os

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

HF_API_KEY = os.environ.get("HF_API_KEY")

# Initialize client only if key and OpenAI module are available
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_API_KEY
) if HF_API_KEY and OpenAI else None

def code_task(plan: str) -> str:
    """
    Generate code from a plan. Safe fallback if HF_API_KEY is missing.
    """
    if not client:
        return "HF_API_KEY not set or OpenAI module missing."
    
    try:
        completion = client.chat.completions.create(
            model="moonshotai/Kimi-K2-Instruct-0905",
            messages=[{"role": "user", "content": f"Write code for this plan:\n{plan}"}],
        )
        return completion.choices[0].message
    except Exception as e:
        return f"Error calling HF model: {str(e)}"
