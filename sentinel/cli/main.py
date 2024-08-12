import os
import subprocess
from pathlib import Path
from typing import List

import typer

from sentinel import console

app = typer.Typer()


@app.command()
def main(dir: str = "tests") -> None:
    typer.echo(f"Running tests in directory: {dir}")

    path_to_tests = Path(dir).resolve()
    tests_files: List[str] = []
    for root, _, files in os.walk(path_to_tests):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                tests_files.append(file_path)

    counter = 0
    total_files = len(tests_files)
    for i in range(total_files):
        file = tests_files[i]
        path = f"{dir}{file.split(f"/{dir}")[-1]}"
        console.print_info(f"\n● Executing: {path}")
        counter += 1
        out_text = f"{counter}/{total_files}: {path}"
        try:
            subprocess.run(["python", file], check=True)
            console.print_success(f"✔ {out_text}")
        except Exception:
            console.print_error(f"✘ {out_text}")
