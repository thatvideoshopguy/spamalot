"""Load the file hashes for the exercises. """
from spamalot.utils import compute_file_hash, load_exercise_order


def load_file_hashes(exercises: list) -> dict:
    """Load the file hashes for the exercises.

    Args:
        exercises (list): A list of exercises.

    Returns:
        dict: A dictionary of file paths and their hashes.
    """

    file_hashes_dict = {}
    for exercise in exercises:
        file_path = f"exercises/{exercise}.py"
        file_hash = compute_file_hash(file_path)
        file_hashes_dict[file_path] = file_hash
    return file_hashes_dict


if __name__ == "__main__":
    exercise_list = load_exercise_order("exercises/exercises.yaml")
    file_hashes = load_file_hashes(exercise_list)

    print(f"Initial file hashes: {file_hashes}")
