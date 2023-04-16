""" A file watcher that watches for changes to the exercises.

Typical usage example:
    watcher = Watcher(exercise_order, file_hashes)
    watcher.start()
 """
from pathlib import Path
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
from watchdog.observers import Observer
from utils import clear_screen, check_exercises, compute_file_hash


class Watcher(FileSystemEventHandler):
    """A file watcher that watches for changes to the exercises.

    Attributes:
        exercise_order (list): A list of exercises.
        file_hashes (dict): A dictionary of file paths and their hashes.
    """

    def __init__(self, exercise_order: list, file_hashes: dict) -> None:
        self.exercise_order = exercise_order
        self.file_hashes = file_hashes

    def on_modified(self, event: FileModifiedEvent) -> None:
        """Handle a file modification event.

        Args:
            event (FileModifiedEvent): The file modification event.
        """

        if not isinstance(event, FileModifiedEvent):
            return

        src_path = Path(event.src_path)

        if ".tmp" in src_path.name:
            return

        relative_src_path = src_path.relative_to(Path.cwd())

        initial_file_hash = self.file_hashes[str(relative_src_path)]
        current_file_hash = compute_file_hash(str(relative_src_path))

        if initial_file_hash == current_file_hash:
            # logger.info("File contents of '%s' haven't changed", src_path)
            return
        else:
            # logger.info("File modified: %s", event)

            self.file_hashes[str(relative_src_path)] = current_file_hash

            clear_screen()
            print(check_exercises(self.exercise_order))


def start_watcher(exercise_order: list, file_hashes: dict) -> Observer():
    """Start the file watcher.

    Args:
        exercise_order (list): A list of exercises.
        file_hashes (dict): A dictionary of file paths and their hashes.

    Returns:
        Observer: The file watcher.
    """
    event_handler = Watcher(exercise_order, file_hashes)
    path = "exercises"

    observer = Observer()
    observer.schedule(
        event_handler,
        path,
        recursive=True,
    )
    observer.start()

    return observer
