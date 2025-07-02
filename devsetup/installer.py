import subprocess
from rich import print

def run(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[red]❌ Error running: {command}[/red]\n{e}")

def install_tool(tool, os_name):
    print(f"[blue]Installing {tool}...[/blue]")

    if tool == "Node.js":
        if os_name == "windows":
            run("choco install nodejs -y")
        elif os_name == "linux":
            run("curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -")
            run("sudo apt install -y nodejs")
        elif os_name == "darwin":
            run("brew install node")

    elif tool == "Python3":
        if os_name == "windows":
            run("choco install python -y")
        elif os_name == "linux":
            run("sudo apt install -y python3 python3-pip")
        elif os_name == "darwin":
            run("brew install python")

    elif tool == "Git":
        if os_name == "windows":
            run("choco install git -y")
        elif os_name == "linux":
            run("sudo apt install -y git")
        elif os_name == "darwin":
            run("brew install git")

    elif tool == "Docker":
        if os_name == "windows":
            run("choco install docker-desktop -y")
        elif os_name == "linux":
            run("sudo apt install -y docker.io")
        elif os_name == "darwin":
            run("brew install --cask docker")

    else:
        print(f"[yellow]No install command defined for {tool}[/yellow]")

    print(f"[green]✔️ {tool} installed (or already present)[/green]\n")
