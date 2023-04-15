import subprocess
import curses
import io
from typing import Tuple


# SKIP_CHECKS = set()


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
    # print(f"output: {output}")
    return output


def check_exercises(exercise_list: list) -> Tuple[str, int]:
    # Initialize the output buffer
    output_buffer = io.StringIO()

    # all_passed = True
    for exercise in exercise_list:
        output = run_exercise(exercise)
        if output.returncode != 0:
            # print(f"exit code: {output.returncode}")
            output_buffer.write(f"❌ exercises/{exercise}.py failed\n")
            output_buffer.write(output.stderr)
            # all_passed = False
            break  # Stop the loop if the returncode is not equal to zero
        else:
            output_buffer.write(f"✅ exercises/{exercise}.py passed\n")

    # Get the output string and count the number of lines
    output_str = output_buffer.getvalue()
    num_lines = len(output_str.splitlines())

    # Print the output string to the screen
    # print(output_str)
    # print(f"num_lines: {num_lines}")

    # Clear the screen from the current position to the end of the screen
    # stdscr = curses.initscr()
    # stdscr.clrtobot()
    # stdscr.refresh()

    # Print the output string to the screen
    # print(output_str)

    # Clean up curses
    # curses.endwin()

    return output_str, num_lines


if __name__ == "__main__":
    exercise_order = ["basics/exercise1", "basics/exercise2", "basics/exercise3"]
    result, lines_length = check_exercises(exercise_order)

    print(result)
    print(f"lines_length: {lines_length}")
