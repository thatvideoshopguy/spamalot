import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
from datetime import datetime, timedelta
import yaml
import subprocess
import os
from subprocess import PIPE, Popen
import hashlib
from utils import clear_screen, load_exercise_order, check_exercises

SKIP_CHECKS = []


# def check_exercises(flake8_check=False):
#     print("Checking exercises...")
#     print(f"SKIP CHECKS: {SKIP_CHECKS}")
#     for exercise in exercises:
#         if exercise not in SKIP_CHECKS:
#             cmd = "python3 exercises/{exercise}.py".format(exercise=exercise)

#             try:
#                 # flake_check(exercise, flake8_check)
#                 exit_code = subprocess.call(
#                     cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
#                 )
#                 if exit_code != 0:
#                     print("exit code: {exit_code}".format(exit_code=exit_code))
#                     print("❌ exercises/{exercise}.py failed".format(exercise=exercise))
#                     return subprocess.check_output(cmd, shell=True)
#                 else:
#                     print("✅ exercises/{exercise}.py passed".format(exercise=exercise))
#                     SKIP_CHECKS.append(exercise)
#             except subprocess.CalledProcessError:
#                 break
#         else:
#             print("✅ exercises/{exercise}.py passed".format(exercise=exercise))


class ModificationWatcher(FileSystemEventHandler):
    def __init__(self, exercises):
        self.last_modified = datetime.now()
        # self.debounce_interval = debounce_interval
        self.file_hashes = {}
        self.exercise_list = exercises

    def compute_file_hash(self, file_path):
        hasher = hashlib.md5()
        with open(file_path, "rb") as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def on_modified(self, event):
        if not isinstance(event, FileModifiedEvent):
            return

        if ".tmp" in event.src_path:
            return

        current_time = datetime.now()
        # time_elapsed = current_time - self.last_modified

        # if time_elapsed.total_seconds() < self.debounce_interval:
        #     return

        file_hash = self.compute_file_hash(event.src_path)
        print("file_hash: {file_hash}".format(file_hash=file_hash))

        if (
            event.src_path in self.file_hashes
            and self.file_hashes[event.src_path] == file_hash
        ):
            return  # file contents haven't changed

        self.file_hashes[event.src_path] = file_hash
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
    event_handler = ModificationWatcher(exercises)
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
