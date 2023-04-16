# Spamalot

[![License](https://img.shields.io/github/license/thatvideoshopguy/spamalot.svg)](https://github.com/thatvideoshopguy/spamalot/blob/main/LICENSE)
[![Code Climate](https://codeclimate.com/github/thatvideoshopguy/spamalot/badges/gpa.svg)](https://codeclimate.com/github/thatvideoshopguy/spamalot)
[![Issues](https://img.shields.io/github/issues/thatvideoshopguy/spamalot.svg)](https://github.com/thatvideoshopguy/spamalot/issues)

## What is this?

Spamalot is a Python-based interactive learning tool designed to help new Python programmers learn and practice syntax and error fixing through a series of exercises. The exercises are a combination of Python syntax and common errors that new programmers make.

## How does it run?

Spamalot watches the `exercises/` folder for changes. When you make the necessary changes for an exercise to pass and save the file, you'll see that the exercise has passed. Then it will start the next exercise in the folder.

## How do I get started?

First, make sure you have Python 3 installed on your system.

Next, create a virtual environment for Python using `venv`. Navigate to the project directory and run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

Then install the dependencies in the requirements.txt file with pip:

```bash
pip install -r requirements.txt
```

Now you can run the main.py program with Python:

```bash
python spamalot/main.py
```

### How do I work on the exercises?

In the `exercises/` folder, there is a series of Python scripts that the program will attempt to run. When it encounters a script with an error, it will stop and show you the traceback of what happened. Modify the file to fix the error and make the script run.

Every time you modify a file in the exercises, the program will detect it and attempt to run the latest failing test.

### Credits

Spamalot is originally a fork of by [Egglings](https://github.com/numbertheory/egglings) by JP Etcheber and [Rustlings](https://github.com/rust-lang/rustlings). A big thank you to the authors and contributors of these projects for their inspiration.
