import os
from agents.planner import plan_project
from agents.coder import generate_code
from agents.debugger import fix_code
from core.executor import run_python_file

JOBS_DIR = "jobs"

if not os.path.exists(JOBS_DIR):
    os.makedirs(JOBS_DIR)


def run_job(goal: str):

    print("Planning project...")
    plan = plan_project(goal)

    print("Plan:")
    print(plan)

    print("Generating code...")
    code = generate_code(plan)

    file_path = os.path.join(JOBS_DIR, "app.py")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

    for attempt in range(5):

        print(f"\nExecution attempt {attempt + 1}")

        result = run_python_file(file_path)

        if result["success"]:
            print("SUCCESS ✅")
            print(result["stdout"])
            return "Completed successfully"

        print("Error detected. Fixing...")
        print(result["stderr"])

        code = fix_code(code, result["stderr"])

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)

    return "Failed after 5 attempts ❌"


if __name__ == "__main__":
    goal_input = input("Enter project goal: ")
    run_job(goal_input)
