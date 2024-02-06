import csv
import os
from .patient import Gender, Patient
from rich.prompt import Prompt
from rich.console import Console

console = Console()

def clear_console() -> None:
    # I'm assuming this script is being run on Windows
    os.system('cls')

def print_welcome() -> None:
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

def display_menu() -> None:
    console.print("[yellow]Menu choices:")
    console.print("[bold green]\t1. Create a patient entry")
    console.print("[bold blue]\t2. View the patient entries")
    console.print("[bold red]\t3. Exit")

def get_menu_response() -> int:
    display_menu()
    return int(
        Prompt.ask("Please enter a choice", choices=['1', '2', '3'])
    )

def new_patient() -> Patient:
    # TO DO
    # Implement the prompts to get the patient information
    return Patient("", 0, Gender.Other, "")

def show_patients(patient_list: list[Patient]):
    console.print(patient_list)
    # TO DO
    # Print a table nicely