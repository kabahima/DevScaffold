import questionary
from rich.console import Console
from devsetup.installer import install_tools, install_databases, install_containers
from devsetup.bootstrap import scaffold_project

console = Console()

def main():
    console.rule("[bold blue]Welcome to DevSetup CLI")

    choices = [
        "Install Developer Tools",
        "Scaffold New Project",
        "Setup Containers & Kubernetes",
        "Install Databases",
        "Exit"
    ]

    while True:
        choice = questionary.select("Choose an option:", choices=choices).ask()
        if choice == "Install Developer Tools":
            install_tools()
        elif choice == "Scaffold New Project":
            scaffold_project()
        elif choice == "Setup Containers & Kubernetes":
            install_containers()
        elif choice == "Install Databases":
            install_databases()
        elif choice == "Exit":
            console.print("[green]Goodbye!")
            break

if __name__ == "__main__":
    main()