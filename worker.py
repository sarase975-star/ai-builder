# worker.py

from agents.planner import plan_project
from agents.coder import generate_code
from agents.debugger import fix_code
from core.executor import run_python_file

def run_job(goal):

    print("Planning...")
    plan = plan_project(goal)

    print("Generating code...")
    code = generate_code(plan)

    with open("jobs/app.py", "w") as f:
        f.write(code)

    for i in range(5):

        print(f"Execution attempt {i+1}")
        result = run_python_file("jobs/app.py")

        if result["success"]:
            print("SUCCESS")
            return

        print("Fixing errors...")
        code = fix_code(code, result["stderr"])

        with open("jobs/app.py", "w") as f:
            f.write(code)

    print("FAILED after max retries")
