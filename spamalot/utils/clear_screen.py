"""Clear the shell screen """
import os
import subprocess


def clear_screen() -> None:
    """Clear the screen using the appropriate command for the OS"""
    if os.name == "nt":
        subprocess.run("cls", shell=True, check=True)
    else:
        subprocess.run("clear", shell=True, check=True)
