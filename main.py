import src.functions as functions
from dotenv import dotenv_values

# get the path for the CSV file from the .env file
config = dotenv_values(".env")
PATIENT_DATA_CSV_PATH = config['PATIENT_DATA_CSV_PATH']

def main():
    # print welcome message
    functions.print_welcome()
    # parse the CSV file
    patient_list = functions.parse_data(PATIENT_DATA_CSV_PATH)
    # loop displaying the menu and getting user response
    while True:
        match functions.get_menu_response():
            case 1:
                patient_list.append(functions.new_patient())
            case 2:
                functions.show_patients(patient_list)
            case _:
                break
    # TO DO
    # save the patient data back to the file
    # display exit message

if __name__ == "__main__":
    main()