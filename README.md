
# Employee Ratings Application Documentation
Here is an explanation of our application's code. 

**Note:** This documentation was created using ChatGPT (with some edits, of course.)

## Description

This script, titled "Assignment 08," serves as the final project for the Fin110B course. It is an employee ratings application that allows users to manage and interact with employee data. The script provides functionality to display current data, input new employee rating data, save data to a file, and exit the program.

______________________________________________________________________________________

## ChangeLog

- **SGhafir**, *12/10/23*: Created the script.

_______________________________________________________________________________________


## Usage

Run this script to execute the employee ratings application.

## Data Configuration

- `FILE_NAME`: The default file name for storing employee data is 'EmployeeRatings.json'.

## Menu Options

The script presents a menu with the following options:

1. **Show current employee rating data**: Display the current employee rating data.

2. **Enter new employee rating data**: Allow the user to input new employee rating data and display the changes.

3. **Save data to a file**: Save the current employee data to a file.

4. **Exit the program**: End the program.

## Execution Flow

1. The script imports necessary modules (`json`, `date`, `processing_classes`, `presentation_classes`, and `Employee` from `data_classes`).

2. Initializes variables, including the file name (`FILE_NAME`), the menu string (`MENU`), an empty list for employee data (`employees`), and an empty string for menu choice (`menu_choice`).

3. Reads employee data from the file (`EmployeeRatings.json`) using the `FileProcessor` class from `processing_classes`.

4. Enters a loop to repeatedly present the menu and perform actions based on user input.

5. Depending on the user's menu choice, the script performs the following actions:
   - Option 1: Displays the current employee data.
   - Option 2: Allows the user to input new employee rating data and displays the changes.
   - Option 3: Saves the current employee data to a file (`EmployeeRatings.json`).
   - Option 4: Ends the program by breaking out of the loop.

6. The script handles exceptions during menu operations and outputs error messages using the `IO` class from `presentation_classes`.

## Presentation Classes

### `IO` Class

A collection of presentation layer functions that manage user input and output.

- `output_error_messages(message: str, error: Exception = None)`: Displays custom error messages to the user. The function takes a user-friendly message and an optional technical error message.

- `output_menu(menu: str)`: Displays the menu of choices to the user.

- `input_menu_choice()`: Gets a menu choice from the user. It checks if the user input is a valid menu choice and handles exceptions accordingly.

- `output_employee_data(employee_data: list)`: Displays employee data to the user.

- `input_employee_data(employee_data: list, employee_type: Employee)`: Gets first name, last name, review date, and review rating from the user. It includes error handling for incorrect data types and non-specific errors.

## Processing Classes

### `FileProcessor` Class

A collection of processing layer functions that work with JSON files.

- `read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee)`: Reads data from a JSON file and loads it into a list of dictionary rows. It handles exceptions for file not found and non-specific errors.

- `write_employee_data_to_file(file_name: str, employee_data: list)`: Writes data to a JSON file with data from a list of dictionary rows. It includes error handling for invalid JSON format, file permission issues, and non-specific errors.

## Data Classes

### `Person` Class

A class representing person data.

Properties:
- `first_name (str)`: The person's first name.
- `last_name (str)`: The person's last name.

Getters and Setters:
- The `first_name` and `last_name` properties have getters and setters that enforce certain data validation rules. The first and last names must not contain numbers.

### `Employee` Class

A class representing employee data.

Properties:
- `first_name (str)`: The employee's first name.
- `last_name (str)`: The employee's last name.
- `review_date (date)`: The data of the employee review.
- `review_rating (int)`: The review rating of the employee's performance (1-5).

Getters and Setters:
- The `review_date` property has a setter that validates the date format.
- The `review_rating` property has a setter that validates the rating value to be within the range of 1 to 5.
