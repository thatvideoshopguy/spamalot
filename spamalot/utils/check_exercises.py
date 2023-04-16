""" Run and check the exercises in the exercise list.

This module runs the exercises in the exercise list and checks the output.

Typical usage example:
    exercise_order = ["basics/exercise1", "basics/exercise2", "basics/exercise3"]
    print(check_exercises(exercise_order))
"""
from pathlib import Path
import subprocess
from typing import List


def run_exercise(exercise: str) -> subprocess.CompletedProcess:
    """Run the exercise.

    Args:
        exercise (str): The exercise to run.

    Returns:
        subprocess.CompletedProcess: The output of the exercise.
    """
    exercise_path = Path("exercises") / f"{exercise}.py"
    cmd = f"python3 {exercise_path}"
    output = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    return output


def check_exercises(exercise_list: List[str]) -> str:
    """Check the exercises in the exercise list.

    Args:
        exercise_list (list): A list of exercises.

    Returns:
        str: The output of the exercises.
    """
    output_buffer = []

    for exercise in exercise_list:
        output = run_exercise(exercise)
        if output.returncode != 0:
            output_buffer.append(f"❌ exercises/{exercise}.py failed\n")
            output_buffer.append(output.stderr)
            break
        else:
            output_buffer.append(f"✅ exercises/{exercise}.py passed\n")

    return "".join(output_buffer)


if __name__ == "__main__":
    exercise_order = ["basics/exercise1", "basics/exercise2", "basics/exercise3"]
    print(check_exercises(exercise_order))
