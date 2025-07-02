import platform
import questionary
from devsetup.installer import install_tool
from rich import print

def main():
    print("[bold green]🛠 DevSetup CLI Tool[/bold green]\n")

    tools = questionary.checkbox(
        "Select tools to install:",
        choices=["Node.js", "Python3", "Git", "Docker"]
    ).ask()

    if not tools:
        print("[yellow]⚠️ No tools selected. Exiting.[/yellow]")
        return

    os_name = platform.system().lower()  # 'windows', 'linux', or 'darwin'
    print(f"[cyan]Detected OS: {os_name}[/cyan]\n")

    for tool in tools:
        install_tool(tool, os_name)

    print("\n[bold green]✅ Setup complete![/bold green]")
