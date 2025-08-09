import shutil
import subprocess
import sys
import platform
from rich.console import Console

console = Console()

def is_python_installed():
    return shutil.which("python3") or shutil.which("python")

def install_python():
    os_type = platform.system()
    console.print("[yellow]Attempting to install Python...")
    try:
        if os_type == "Windows":
            if shutil.which("choco"):
                subprocess.run("choco install python -y", shell=True, check=True)
            else:
                console.print("[red]Chocolatey not found. Please install Python manually.")
        elif os_type == "Darwin":
            if shutil.which("brew"):
                subprocess.run("brew install python", shell=True, check=True)
            else:
                console.print("[red]Homebrew not found. Please install Python manually.")
        elif os_type == "Linux":
            if shutil.which("apt"):
                subprocess.run("sudo apt update && sudo apt install -y python3 python3-pip", shell=True, check=True)
            else:
                console.print("[red]APT not found. Please install Python manually.")
        console.print("[green]Python installed. Please restart the tool.")
    except subprocess.CalledProcessError:
        console.print("[red]Automatic installation failed. Please install Python manually.")

    sys.exit(0)

if __name__ == "__main__":
    if not is_python_installed():
        console.print("[red]Python is not installed on your system.")
        install_python()
    else:
        from devsetup.cli import main
        main()
