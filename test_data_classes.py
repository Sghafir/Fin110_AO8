from data_classes import Person
from data_classes import Employee

def test_person_class():

    print("Testing Person class:")
    person = Person("Su", "Salias")
    print(person)  # Should print "Su,Salies"
    try:
        # set an invalid first name
        person.first_name = "123"
    except ValueError as e:
        print(f"Error: {e}")  # Should print "Error: The first name should not contain numbers."
    try:
        # invalid last name
        person.last_name = "456"
    except ValueError as e:
        print(f"Error: {e}")  # Should print "Error: The last name should not contain numbers."


def test_employee_class():
    print("Testing employee class:")
    employee = Employee("Su", "Salias", "1900-01-01", 3)
    print(employee)  # Should print "Su,Salias, 1900-01-01, 3
    try:
        # set an invalid review date
        employee.review_date = "12"
    except ValueError as e:
        print(f"Error: {e}")  # Should print "Incorrect data format, should be YYYY-MM-DD"
    try:
        # set an invalid review rating
        employee.review_rating = "A"
    except ValueError as e:
        print(f"Error: {e}")  # Should print  "Please choose only values 1 through 5"



#Running cases

test_person_class()
test_employee_class()
