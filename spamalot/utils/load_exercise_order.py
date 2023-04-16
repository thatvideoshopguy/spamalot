"""This module contains a function to load the exercises.yaml file. 

Typical usage example:
    exercise_list = load_exercise_order("exercises/exercises.yaml")
"""
import yaml


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


if __name__ == "__main__":
    exercise_list = load_exercise_order("exercises/exercises.yaml")
    print(f"exercise_list: {exercise_list}")
