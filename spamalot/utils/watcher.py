# from datetime import datetime, timedelta
import os.path
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
from watchdog.observers import Observer

# from .logger import main_logger as logger
from utils import clear_screen, check_exercises, compute_file_hash


class Watcher(FileSystemEventHandler):
    def __init__(
        self, exercise_order: list, file_hashes: dict, lines_length: int
    ) -> None:
        # self.last_modified = datetime.now()
        self.exercise_order = exercise_order
        self.file_hashes = file_hashes
        self.lines_length = lines_length

    def on_modified(self, event: FileModifiedEvent) -> None:
        if not isinstance(event, FileModifiedEvent):
            return

        if ".tmp" in event.src_path:
            return

        # current_time = datetime.now()
        src_path = os.path.relpath(event.src_path, start=os.getcwd())

        initial_file_hash = self.file_hashes[src_path]
        current_file_hash = compute_file_hash(src_path)

        if initial_file_hash == current_file_hash:
            # logger.info("File contents of '%s' haven't changed", src_path)
            return
        else:
            # logger.info("File modified: %s", event)

            self.file_hashes[src_path] = current_file_hash
            # self.last_modified = current_time

            # print("Running exercise check on modified file")
            # print(self.exercise_list)
            clear_screen(self.lines_length)
            result, new_lines_length = check_exercises(self.exercise_order)
            print(result)
            self.lines_length = new_lines_length


def start_watcher(
    exercise_order: list, file_hashes: dict, lines_length: int
) -> Observer():
    event_handler = Watcher(exercise_order, file_hashes, lines_length)
    observer = Observer()
    observer.schedule(
        event_handler,
        path="/Users/kylestevenson/Documents/Github/spamalot/exercises/",
        recursive=False,
    )
    observer.start()
    return observer
