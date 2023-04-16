"""This is the main entry point for the spamalot application.

Typical usage example:
    python3 -m spamalot.main
"""
from utils import (
    load_exercise_order,
    check_exercises,
    clear_screen,
    load_file_hashes,
    start_watcher,
)


def main():  # pylint: disable=missing-function-docstring
    exercises = load_exercise_order("exercises/exercises.yaml")
    file_hashes = load_file_hashes(exercises)

    watcher = start_watcher(exercises, file_hashes)

    try:
        clear_screen()
        print(check_exercises(exercises))

        while watcher.is_alive():
            watcher.join(1)

    except KeyboardInterrupt:
        watcher.stop()
        exit(0)

    watcher.join()


if __name__ == "__main__":
    main()
