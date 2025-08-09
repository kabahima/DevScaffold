import platform, shutil, subprocess
from rich.console import Console
import questionary

console = Console()

OS = platform.system()

def is_installed(tool):
    return shutil.which(tool) is not None

def run_install(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
        console.print(f"[green]Installed with: {cmd}")
    except subprocess.CalledProcessError:
        console.print(f"[red]Failed: {cmd}")

def get_install_cmd(tool):
    if OS == "Windows":
        return f"choco install {tool} -y"
    elif OS == "Darwin":
        return f"brew install {tool}"
    else:
        return f"sudo apt install {tool} -y"

def install_tools():
    tools = questionary.checkbox("Select tools to install:", choices=["node", "python3", "git", "docker"]).ask()
    for tool in tools:
        if is_installed(tool):
            console.print(f"[yellow]{tool} already installed")
        else:
            run_install(get_install_cmd(tool))

def install_databases():
    dbs = questionary.checkbox("Select databases:", choices=["postgresql", "mysql", "sqlite3", "mongodb", "redis"]).ask()
    for db in dbs:
        if is_installed(db):
            console.print(f"[yellow]{db} already installed")
        else:
            run_install(get_install_cmd(db))

def install_containers():
    tools = questionary.checkbox("Install container tools:", choices=["podman", "kubectl", "minikube", "microk8s"]).ask()
    for tool in tools:
        if is_installed(tool):
            console.print(f"[yellow]{tool} already installed")
        else:
            run_install(get_install_cmd(tool))