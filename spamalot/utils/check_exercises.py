import subprocess

# SKIP_CHECKS = set()


def run_exercise(exercise):
    cmd = f"python3 exercises/{exercise}.py"
    output = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    print(f"output: {output}")
    return output


def check_exercises(exercise_list):
    all_passed = True
    for exercise in exercise_list:
        # if exercise not in SKIP_CHECKS:
        output = run_exercise(exercise)
        if output.returncode != 0:
            print(f"exit code: {output.returncode}")
            print(f"❌ exercises/{exercise}.py failed")
            print(output.stderr)
            all_passed = False
            break  # Stop the loop if the returncode is not equal to zero
        else:
            print(f"✅ exercises/{exercise}.py passed")
            # SKIP_CHECKS.add(exercise)
    # else:
    #     print(f"✅ exercises/{exercise}.py passed")
    return all_passed


if __name__ == "__main__":
    exercise_order = ["basics/exercise1", "basics/exercise2", "basics/exercise3"]
    check_exercises = check_exercises(exercise_order)
    print(check_exercises)
