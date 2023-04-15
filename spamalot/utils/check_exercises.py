import subprocess
import io


def run_exercise(exercise: str) -> subprocess.CompletedProcess:
    cmd = f"python3 exercises/{exercise}.py"
    output = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    return output


def check_exercises(exercise_list: list) -> str:
    """Check the exercises in the exercise list.

    Args:
        exercise_list (list): A list of exercises.

    Returns:
        str: The output of the exercises.
    """
    output_buffer = io.StringIO()

    for exercise in exercise_list:
        output = run_exercise(exercise)
        if output.returncode != 0:
            output_buffer.write(f"❌ exercises/{exercise}.py failed\n")
            output_buffer.write(output.stderr)
            break
        else:
            output_buffer.write(f"✅ exercises/{exercise}.py passed\n")

    return output_buffer.getvalue()


if __name__ == "__main__":
    exercise_order = ["basics/exercise1", "basics/exercise2", "basics/exercise3"]
    print(check_exercises(exercise_order))
