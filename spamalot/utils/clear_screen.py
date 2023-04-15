"""Clear the shell screen """
import os
import subprocess
import curses
import sys


def clear_screen(num_lines: int) -> None:
    """Clear the specified number of lines from the current cursor position"""
    # if os.name == "nt":
    #     subprocess.run("cls", shell=True, check=True)
    # else:
    #     subprocess.run("clear", shell=True, check=True)

    # Save the current cursor position
    sys.stdout.write("\033[s")

    # Move the cursor up by num_lines
    sys.stdout.write(f"\033[{num_lines}A")

    # Clear lines one by one
    for _ in range(num_lines):
        sys.stdout.write("\033[2K")  # Clear the entire line
        sys.stdout.write("\033[1A")  # Move the cursor up by one line

    # Restore the cursor position
    sys.stdout.write("\033[u")

    sys.stdout.flush()
