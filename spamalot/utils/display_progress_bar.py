""" Shows the progress of the user through the exercises. """


def display_progress_bar(passed_tests, total_exercises, bar_length=60):
    completed_exercises = len(passed_tests)
    progress = completed_exercises / total_exercises
    completed_length = int(bar_length * progress)
    remaining_length = bar_length - completed_length

    progress_bar = f"[{'#' * completed_length}{'-' * remaining_length}] {completed_exercises}/{total_exercises}"
    print(f"Progress: {progress_bar}")


if __name__ == "__main__":
    display_progress_bar([1, 2, 3], 10, 20)
