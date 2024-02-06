import unittest
import src.functions as functions
from dotenv import dotenv_values

# get the path for the CSV file from the .env file
config = dotenv_values(".env")
TESTS_PATIENT_DATA_CSV_PATH = config['TESTS_PATIENT_DATA_CSV_PATH']

class TestFunctions(unittest.TestCase):
    def setUp(self):
        with open(TESTS_PATIENT_DATA_CSV_PATH, 'w') as f:
            f.write(
                "John Smith,35,Male,01234567890\n"
                "Jane Doe,28,Female,07890123456\n"
                "Michael Johnson,42,Male,07654321098\n"
                "Emily Davis,50,Female,02078906543\n"
                "Robert Miller,22,Male,07123456789\n"
                "Sara Wilson,40,Other,09876543210\n"
                "Alice Turner,32,Female,06543210987\n"
            )

    def test_parse_data(self):
        patients_list = functions.parse_data(TESTS_PATIENT_DATA_CSV_PATH)
        self.assertEqual(patients_list[0].name, 'John Smith')
        self.assertEqual(patients_list[0].gender.name, 'Male')
        # etc.
    
    #can write other methods too to test other things