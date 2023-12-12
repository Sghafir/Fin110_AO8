import unittest
import tempfile
import json
import data_classes as data
from processing_classes import FileProcessor
from data_classes import Employee

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "Su", "LastName": "Salias", "ReviewDate": "1900-05-19", "ReviewRating": 4},
            {"FirstName": "Vic", "LastName": "Vu", "ReviewDate": "1900-05-18", "ReviewRating": 3}
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)


        # Call the read_data_from_file method and check if it returns the expected data
        # added employees list here to capture the data read from the file

        employees = []
        employees = FileProcessor.read_employee_data_from_file(self.temp_file_name, employees, Employee)


        # Assert that the employee_data list contains the expected employee objects
        # Need to add a forloop here to make sure that each dictionary key is equal to each object

        self.assertEqual(len(sample_data), len(employees))
        for row in range(len(sample_data), len(employees)):
          self.assertEqual(sample_data[row]["FirstName"], employees[row].first_name)
          self.assertEqual(sample_data[row]["LastName"], employees[row].last_name)
          self.assertEqual(sample_data[row]["ReviewDate"], employees[row].review_date)
          self.assertEqual(sample_data[row]["ReviewRating"], employees[row].review_rating)


    def test_write_data_to_file(self):
        # Create some sample student objects
        # Need to add the Employee class here so the program can identify object formatting
        sample_employee = [
            Employee("Vic", "Vu", "2023-05-19", 4),
            Employee("Su", "Salias", "2023-08-20", 5)
        ]

        # Call the write_data_to_file method to write the data to the temporary file

        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employee)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employee))

        #need another for loop here to verify that the file data is equal to sample employee

        for row in range(len(sample_employee), len(file_data)):
            self.assertEqual(file_data[row]["FirstName"],sample_employee[row].first_name)
            self.assertEqual(file_data[row]["LastName"],sample_employee[row].last_name)
            self.assertEqual(file_data[row]["ReviewDate"], sample_employee[row].review_date)
            self.assertEqual(file_data[row]["ReviewRating"], sample_employee[row].review_rating)

if __name__ == "__main__":
    unittest.main()

