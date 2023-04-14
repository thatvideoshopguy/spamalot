from .load_exercise_order import load_exercise_order, get_initial_file_hashes
from .clear_screen import clear_screen
from .check_exercises import check_exercises
from .file_hash import compute_file_hash
from .watcher import start_watcher

# from .custom_logger import setup_logger
from .logger import setup_logger

main_logger = setup_logger(__name__, log_file="output.log")

# from .lint_exercise import lint_exercise
