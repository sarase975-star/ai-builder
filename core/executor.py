# core/executor.py

import subprocess

def run_python_file(path):

    try:
        result = subprocess.run(
            ["python", path],
            capture_output=True,
            text=True,
            timeout=20
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except Exception as e:
        return {
            "success": False,
            "stderr": str(e)
        }
