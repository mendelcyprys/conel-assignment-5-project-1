import csv
import os
from .patient import Gender, Patient
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.console import Console
from rich.panel import Panel

console = Console()

def clear_console() -> None:
    # I'm assuming this script is being run on Windows
    os.system('cls')

def display_welcome_message() -> None:
    """Prints a welcome message to the console"""
    clear_console()
    console.rule(
        "[yellow]Welcome to the patient data management program!",
        style="yellow",
    )
    console.print()

def parse_data(data_path: str) -> list[Patient]:
    """Parses the data in the CSV file at data_path
    and returns a list of Patient objects
    """
    patient_list = []
    try:
        with open(data_path, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                # append the line to the patient list
                patient_list.append(
                    # I assume here that the CSV file is valid
                    # otherwise an error will be raised
                    Patient(row[0], int(row[1]), Gender[row[2]], row[3])
                )
    except FileNotFoundError:
        # if file isn't found, create it
        open(data_path, 'x')
    return patient_list

def write_data(patient_list: list[Patient], data_path: str) -> None:
    """Writes the data back to the CSV file"""
    with open(data_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for patient in patient_list:
            # append the line to the patient list
            writer.writerow(
                [
                    patient.name,
                    str(patient.age),
                    patient.gender.name,
                    patient.contact_number,
                ]
            )

def display_menu() -> None:
    console.print(
        Panel(
            "[bold green]1. Create a new patient entry\n"
            "[bold blue]2. View the patient entries\n"
            "[bold red]3. Exit",
            title="[yellow]Menu choices",
            width=60,
        )
    )

def get_menu_response() -> int:
    display_menu()
    return int(
        Prompt.ask("Please enter a choice", choices=['1', '2', '3'])
    )

def new_patient() -> Patient:
    console.print()
    new_patient = dict()
    new_patient["name"] = Prompt.ask("Enter the patient's name").strip()
    while new_patient["name"] == "":
        console.print("[red]Please enter a valid non empty name")
        new_patient["name"] = Prompt.ask("Enter the patient's name").strip()
    new_patient["age"] = IntPrompt.ask("Enter the patient's age")
    while new_patient["age"] < 0:
        console.print("[red]Please enter a valid non negative integer number")
        new_patient["age"] = IntPrompt.ask("Enter the patient's age")
    new_patient["gender"] = Gender[
        Prompt.ask(
            "Enter the patient's gender",
            choices=['Male', 'Female', 'Other']
        ).strip()
    ]
    new_patient["contact_number"] = Prompt.ask("Enter the patient's contact number").strip()
    # perhaps we can add sometime a regex check on the contact number format
    # but for now I will accept any string
    console.print()
    return Patient(**new_patient)

def show_patients(patient_list: list[Patient]):
    console.print()
    table = Table(title="Patient data")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Age", justify="right", style="magenta")
    table.add_column("Gender", style="green")
    table.add_column("Contact Number", justify="right", style="cyan")
    for patient in patient_list:
        table.add_row(
            patient.name,
            str(patient.age),
            patient.gender.name,
            patient.contact_number,
        )
    console.print(table)
    console.print()

def display_exit_message() -> None:
    console.print("[green]\nData saved to file")
    console.print("[green]Goodbye!\n")