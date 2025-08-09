import os
from rich.console import Console
import questionary

console = Console()

def scaffold_project():
    name = questionary.text("Project name:").ask()
    ptype = questionary.select("Project type:", choices=["Python", "Node.js", "Empty"]).ask()
    path = os.path.abspath(name)
    os.makedirs(path, exist_ok=True)

    dirs = ["src", "tests"]
    for d in dirs:
        os.makedirs(os.path.join(path, d), exist_ok=True)

    with open(os.path.join(path, "README.md"), "w") as f:
        f.write(f"# {name}\n")

    with open(os.path.join(path, ".gitignore"), "w") as f:
        f.write("__pycache__/\nnode_modules/\n.env\n")

    if questionary.confirm("Initialize git repo?").ask():
        subprocess.run("git init", cwd=path, shell=True)

    console.print(f"[green]Project '{name}' scaffolded at {path}")
