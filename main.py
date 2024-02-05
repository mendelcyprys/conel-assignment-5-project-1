import src.functions as functions
from dotenv import dotenv_values

config = dotenv_values(".env")
PATIENT_DATA_CSV_PATH = config['PATIENT_DATA_CSV_PATH']

def main():
    functions.print_hello_world()

if __name__ == "__main__":
    main()