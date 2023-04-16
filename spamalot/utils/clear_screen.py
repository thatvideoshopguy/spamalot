"""Clear the shell screen """
import os
import subprocess


def clear_screen() -> None:
    """Clear the shell screen

    If the OS is Windows, use the 'cls' command. Otherwise, use the 'clear' command.
    """
    if os.name == "nt":
        subprocess.run("cls", shell=True, check=True)
    else:
        subprocess.run("clear", shell=True, check=True)
