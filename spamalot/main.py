"""Main entry point for the spamalot application. """
import time
from utils import (
    load_exercise_order,
    check_exercises,
    load_file_hashes,
    start_watcher,
)


def main():
    """Main entry point for the spamalot application."""

    exercises = load_exercise_order("exercises/exercises.yaml")
    file_hashes = load_file_hashes(exercises)

    observer = start_watcher(exercises, file_hashes)

    try:
        check_exercises(exercises)

        # if exercise_check:
        #     print("printing exercise check")
        #     # print(exercise_check)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        exit(0)
    observer.join()


if __name__ == "__main__":
    main()
