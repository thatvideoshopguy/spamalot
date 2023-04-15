from .load_exercise_order import load_exercise_order
from .load_file_hashes import load_file_hashes
from .clear_screen import clear_screen
from .check_exercises import check_exercises
from .compute_file_hash import compute_file_hash
from .watcher import start_watcher
from .logger import setup_logger

main_logger = setup_logger(__name__, log_file="output.log")
