"""Run the five CSV and SQLite examples in order."""

from pathlib import Path
import subprocess
import sys


# Find the scripts even when this launcher is run from another folder.
SCRIPT_DIR = Path(__file__).resolve().parent

# Start with fresh CSV files, then load, query and modify the database.
SCRIPTS = [
    "01_create_csv.py",
    "02_read_csv.py",
    "03_create_database.py",
    "04_select_data.py",
    # "04_select_data_solutions.py",
    "05_modify_data.py",
]


def main():
    for filename in SCRIPTS:
        print(f"\nExécution : {filename}", flush=True)

        # sys.executable uses the current Python environment.
        # check=True stops the sequence if a script fails.
        subprocess.run(
            [sys.executable, str(SCRIPT_DIR / filename)],
            cwd=SCRIPT_DIR,
            check=True,
        )


if __name__ == "__main__":
    main()
