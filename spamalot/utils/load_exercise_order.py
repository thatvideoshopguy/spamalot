"""This module contains a function to load the exercises.yaml file. """
import yaml
from .file_hash import compute_file_hash


def load_exercise_order(exercises_yaml: str) -> list:
    """Load the exercises.yaml file and return the list of exercises.

    Args:
        exercises_yaml (str): The path to the exercises.yaml file.

    Returns:
        list: A list of exercises.
    """

    with open(exercises_yaml, encoding="utf-8") as yaml_file:
        exercises_data = yaml.safe_load(yaml_file)
    return exercises_data.get("exercises", [])


def get_initial_file_hashes(exercise_list):
    file_hashes = {}
    for exercise in exercise_list:
        file_path = f"exercises/{exercise}.py"
        file_hash = compute_file_hash(file_path)
        file_hashes[file_path] = file_hash
    return file_hashes


if __name__ == "__main__":
    exercise_list = load_exercise_order("exercises/exercises.yaml")
    print(f"exercise_list: {exercise_list}")

    file_hashes = get_initial_file_hashes(exercise_list)
    print(f"Initial file hashes: {file_hashes}")
