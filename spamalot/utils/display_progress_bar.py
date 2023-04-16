"""Shows the progress of the user through the exercises.

Typical usage example:
    print(display_progress_bar([1, 2, 3], 10, 20))
"""


def display_progress_bar(passed_exercises, total_exercises, bar_length=60) -> str:
    """Display the progress of the user through the exercises.

    Args:
        passed_exercises (int): The number of exercises the user has passed.
        total_exercises (int): The total number of exercises.
        bar_length (int): The length of the progress bar.

    Returns:
        str: The progress bar.
    """
    progress = passed_exercises / total_exercises
    completed_length = int(bar_length * progress)
    remaining_length = bar_length - completed_length

    progress_bar = f"Progress: [{'#' * completed_length}{'-' * remaining_length}] "
    progress_bar += f"{passed_exercises}/{total_exercises}"

    return progress_bar


if __name__ == "__main__":
    print(display_progress_bar(3, 10, 20))
