# Week 2 Lecture Exercises

This repository contains lecture exercises for Week 2 of Chem 274A.
To complete the lecture exercises, clone this repository, complete each Python
or shell exercise, and push your work to GitHub.

The Python exercises are tested with
[pytest](https://docs.pytest.org/en/stable/). The shell exercise has a Bash
test script. When you push to GitHub, all exercises will be autograded.

## Making an environment

First make sure you have a Python environment with `pytest` installed. If you
made an environment in Chem 280 that had `pytest`, you may use that. If you
need to make an environment, use these commands to create and activate one:

```bash
conda create --name chem274a conda-forge::python
conda activate chem274a
```

After activating it, install `pytest`:

```bash
conda install conda-forge::pytest
```

The environment is active when `(chem274a)` appears at the beginning of your
terminal prompt. Run `conda deactivate` when you are finished working.

The shell exercise also requires `wget`. Check
whether it is already installed:

```bash
wget --version
```

If that command is not found, install `wget` for your operating system:

On macOS with [Homebrew](https://brew.sh/):

```bash
brew install wget
```

On Ubuntu Linux or Ubuntu under WSL:

```bash
sudo apt update
sudo apt install wget
```

If you use another Linux distribution, install `wget` with that
distribution's system package manager.

## Complete the exercises

Edit only the exercise files.

| File | Task |
| --- | --- |
| `M01Classes01.py` | Define a `Bond` class with `atoms` and `length` instance attributes. |
| `M01Classes02.py` | Add a `stretch` method that changes a bond's length. |
| `M01Classes03.py` | Add a class-level unit conversion factor and support stretching in nanometers. |
| `M01Classes04.py` | Add a `__str__` method to the `Bond` class. |
| `M02Inheritance01.py` | Define and raise an `InvalidDistanceError` for negative distances. |
| `M02Inheritance02.py` | Define an `Ion` class that inherits from `Atom`. |
| `M03Composition01.py` | Define an `Atom` class and compose atoms into a `Molecule` that reports its total electrons. |
| `M04Basics01.sh` | Use `wget` to save the specified URL as `msse_gist.txt`. |

Do not modify files in `tests/`, `.github/scripts/`, or `.github/workflows/`.
Those files define how your work is checked.

## Run the tests locally

Run the Python test suite from the repository directory:

```bash
pytest -v
```

The starter code is intentionally incomplete, so tests will fail at first.
Work through the errors one exercise at a time. To run one Python exercise's
tests, use one of these commands:

```bash
pytest -v tests/test_M01.py::test_01_01
pytest -v tests/test_M01.py::test_01_02
pytest -v -k test_01_03
pytest -v -k test_01_04
pytest -v -k test_02_01
pytest -v -k test_02_02
pytest -v -k test_03_01
```

The `-k` commands run all test cases belonging to the named exercise.

The shell exercise is not run by `pytest`. Test it separately from the
repository directory:

```bash
bash tests/test_M04.sh
```

This command runs `M04Basics01.sh` and checks that it downloaded a file named
`msse_gist.txt`. It requires an internet connection and the `wget` command.
The downloaded file is test output and does not need to be committed.

When all exercises are correct, `pytest -v` should report 16 passing tests and
the shell test should print a passing message. The autograder groups these
checks into eight exercises worth one point each.

## Submit your work

Review your changes, commit them, and push your branch to GitHub:

```bash
git status
git add M01Classes*.py M02Inheritance*.py M03Composition*.py M04Basics*.sh
git commit -m "Complete Week 2 lecture exercises"
git push
```

If a test passes locally but fails on GitHub, confirm that you committed and
pushed the latest version of every exercise file.
