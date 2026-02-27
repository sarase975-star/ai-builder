# agents/planner.py

from core.llm_client import call_model

def plan_project(goal):

    messages = [
        {"role": "system", "content": "You are a senior software architect."},
        {"role": "user", "content": f"Break this into development steps:\n{goal}"}
    ]

    return call_model(
        "moonshotai/Kimi-K2-Instruct-0905:groq",
        messages
    )
