import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
from datetime import datetime, timedelta
import yaml
import subprocess
import os.path
from subprocess import PIPE, Popen
import hashlib
from utils import (
    clear_screen,
    load_exercise_order,
    check_exercises,
    compute_file_hash,
    get_initial_file_hashes,
    start_watcher,
)


if __name__ == "__main__":
    exercises = load_exercise_order("exercises/exercises.yaml")
    file_hashes = get_initial_file_hashes(exercises)
    # event_handler = ModificationWatcher(exercises, file_hashes)
    # observer = Observer()
    # observer.schedule(event_handler, path="exercises/", recursive=False)
    # observer.start()
    observer = start_watcher(exercises, file_hashes)

    try:
        if os.getenv("EGGLINGS_FLAKE8"):
            exercise_check = check_exercises(exercises)
        else:
            print("Running exercise check")
            exercise_check = check_exercises(exercises)
        if exercise_check:
            print("printing exercise check")
            # print(exercise_check)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        exit(0)
    observer.join()
