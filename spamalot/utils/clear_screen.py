"""Clear the shell screen """
import os
import subprocess


def clear_screen() -> None:
    """Clear the specified number of lines from the current cursor position"""
    if os.name == "nt":
        subprocess.run("cls", shell=True, check=True)
    else:
        subprocess.run("clear", shell=True, check=True)
