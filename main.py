import src.functions as functions
from dotenv import dotenv_values

# get the path for the CSV file from the .env file
config = dotenv_values(".env")
PATIENT_DATA_CSV_PATH = config['PATIENT_DATA_CSV_PATH']

def main():
    functions.display_welcome_message()
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
    # save the patient data back to the file
    functions.write_data(patient_list, PATIENT_DATA_CSV_PATH)
    # an alternative way of doing this would be to write to file
    # after every new patient is added
    # but for simplicity we write to file when the script is closed
    functions.display_exit_message()

if __name__ == "__main__":
    main()