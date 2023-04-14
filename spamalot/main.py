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
)


class ModificationWatcher(FileSystemEventHandler):
    def __init__(self, exercise, file_hashes):
        self.last_modified = datetime.now()
        # self.debounce_interval = debounce_interval
        # self.file_hashes = {}
        self.exercise_list = exercises
        self.file_hashes = file_hashes
        print(f"file_hashes: {self.file_hashes}")

    def on_modified(self, event):
        if not isinstance(event, FileModifiedEvent):
            return

        if ".tmp" in event.src_path:
            return

        current_time = datetime.now()
        # time_elapsed = current_time - self.last_modified

        # if time_elapsed.total_seconds() < self.debounce_interval:
        #     return
        print(f"event: {event}")
        src_path = os.path.relpath(event.src_path, start=os.getcwd())
        initial_file_hash = self.file_hashes[src_path]
        current_file_hash = compute_file_hash(src_path)

        print(f"src_path: {src_path}")
        print(f"current file_hash: {current_file_hash}")
        print(f"file_hash: {self.file_hashes[src_path]}")

        if initial_file_hash == current_file_hash:
            return  # file contents haven't changed

        self.file_hashes[src_path] = current_file_hash
        # file_hash(event.src_path) = file_hash
        self.last_modified = current_time

        # On Linux and inside the container, it will double report file changes
        # so this prevents that from happening.
        print("File modified: {event}".format(event=event))
        # date_diff = datetime.now() - self.last_modified
        # if date_diff < timedelta(seconds=1):
        #     print(f"Skipping file change: {date_diff}")
        #     return
        # else:
        #     print("File change detected")
        #     self.last_modified = datetime.now()
        if os.getenv("EGGLINGS_FLAKE8"):
            print("Running flake8 check")
            # clear_screen()
            print(self.exercise_list)
            check_exercises(self.exercise_list)
        else:
            print("Running exercise check on modified file")
            print(self.exercise_list)
            # clear_screen()
            check_exercises(self.exercise_list)


if __name__ == "__main__":
    exercises = load_exercise_order("exercises/exercises.yaml")
    file_hashes = get_initial_file_hashes(exercises)
    event_handler = ModificationWatcher(exercises, file_hashes)
    observer = Observer()
    observer.schedule(event_handler, path="exercises/", recursive=False)
    observer.start()

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
