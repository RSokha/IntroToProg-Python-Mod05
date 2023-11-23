# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RSokha,1/1/2030,Created Script
#   <RSokha>,<11/22/2023>,<Using Functions & Classes>
# ------------------------------------------------------------------------------------------ #

import json

# Constants
MENU = '''---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------'''
FILE_NAME = "Enrollments.json"

# Define the Data Variables and constants -- but commenting out after using them inside class to avoid shadowing.
# Not sure if this is incorrect.
#
# student_first_name: str = ''  # Holds the first name of a student entered by the user.
# student_last_name: str = ''  # Holds the last name of a student entered by the user.
# course_name: str = ''  # Holds the name of a course entered by the user.
# student_data: dict = {}  # one row of student data
# students: list = []  # a table of student data
# csv_data: str = ''  # Holds combined string data separated by a comma.
# json_data: str = ''  # Holds combined string data in a json format.
# file = None  # Holds a reference to an opened file.
# menu_choice: str  # Hold the choice made by the user.


# FileProcessor Class
class FileProcessor:
    @staticmethod # Function to read the file
    def read_data_from_file(file_name: str, student_data: list):
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except FileNotFoundError:
            pass  # File doesn't exist yet; it will be created later
        except Exception as e:
            IO.output_error_messages("Error reading data from file.", e)

    @staticmethod # Function to write/create the file if it doesnt exist then save to it aka option 3
    def write_data_to_file(file_name: str, student_data: list):
        try:
            with open(file_name, 'w') as file:
                json.dump(student_data, file, indent=2)
            print(f"Data saved to {file_name}")
        except Exception as e:
            IO.output_error_messages("Error writing data to file.", e)


# IO Class
class IO:
    @staticmethod # Function to handle output error messages such as selecting invalid option
    def output_error_messages(message: str, error: Exception = None):
        print(f"Error: {message}")
        if error:
            print(f"Details: {error}")

    @staticmethod # Display menu of options once the code runs
    def output_menu(menu: str):
        print(menu)

    @staticmethod # Function that takes user input
    def input_menu_choice():
        return input("Please select an option from the menu:  ")

    @staticmethod # Function that displays output as a result of option "2"
    def output_student_courses(student_data: list):
        for student in student_data:
            print(f"Student Name: {student['first_name']} {student['last_name']}, Course: {student['course']}")

    @staticmethod # Function that displays output as a result of option "1"
    def input_student_data(student_data: list):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        course_name = input("Enter course name: ")
        student_data.append({'first_name': first_name, 'last_name': last_name, 'course': course_name})
        print(f'{first_name} {last_name} is now registered for {course_name}')


# Main Body
class CourseEnrollments:
    students = []

    @staticmethod
    def run():
        FileProcessor.read_data_from_file(FILE_NAME, CourseEnrollments.students)

        menu_choice = ""
        while menu_choice != "4":
            IO.output_menu(MENU)
            menu_choice = IO.input_menu_choice()

            if menu_choice == "1":
                IO.input_student_data(CourseEnrollments.students)
            elif menu_choice == "2":
                IO.output_student_courses(CourseEnrollments.students)
            elif menu_choice == "3":
                FileProcessor.write_data_to_file(FILE_NAME, CourseEnrollments.students)
            elif menu_choice == "4":
                print("Exiting the program. Goodbye!")
            else:
                IO.output_error_messages("Invalid choice. Please select a valid option (1-4).")


if __name__ == "__main__":
    CourseEnrollments.run()
