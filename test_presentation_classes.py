

from unittest.mock import patch
from presentation_classes import IO
import unittest
from data_classes import Employee


class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []
    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')
    def test_input_employee_data(self):
        # Simulate user input for Employee data
        with patch('builtins.input', side_effect=['Su', 'Salias', '1900-05-18', 2]):
            IO.input_employee_data(self.employee_data, employee_type=Employee)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'Su')
            self.assertEqual(self.employee_data[0].last_name, 'Salias')
            self.assertEqual(self.employee_data[0].review_date, '1900-05-18')
            self.assertEqual(self.employee_data[0].review_rating, 2)

if __name__ == "__main__":
    unittest.main()
