"""
Code In Place Final Project:

The application is a console based student grade tracking system.
It is used to track student exam scores for a single class.

Assumptions:

All student numbers and names have been entered for the class.
There are 4 exams per student and default scores are set to None at start

A menu system is used to navigate thorugh the system to display and update data.

Data is saved into a file using JSON format for persistence offline
"""

import json
import sys
import os

STUDENT_RECORD_FILE = "student_data.json"

def main():
    student_records = load_from_file(STUDENT_RECORD_FILE)

    clear_console()
    header()
    user_selection = main_menu()

    if user_selection == "1":
        list_students(student_records, True)
        return_to_main()
    elif user_selection == "2":
        update_student_record(student_records)
    elif user_selection == "3":
        sys.exit("Program Ended!")

# Clears the console window
def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Returns to the main menu
def return_to_main():
    input("Press ENTER to return to the MAIN MENU")
    clear_console()
    main()

# Updates a specific student exam record
def update_student_record(records):
    list_students(records)
    student = input("Please select student number to update: ").upper()

    while student not in records.keys():
        print(student, "is not a valid student number")
        student = input("Please select student number to update: ").upper()
    print()

    print("Student", student, "exam scores")
    list_student_scores(records, student)

    print("\n5. Return to student list\n6. Return to main menu")

    exam_selection = input("\nSelect exam to update score (1, 2, 3, 4): ")

    while exam_selection not in ["1", "2", "3", "4", "5", "6"]:
        print(exam_selection,"is not a valid selection")
        exam_selection = input("Select exam to update score (1, 2, 3, 4): ")

    if exam_selection == "5":
        update_student_record(records)
    elif exam_selection == "6":
        main()
    else:
        exam_number = "exam_" + exam_selection
        update_exam_record(records, student, exam_number)

# Makes changes to specific student exam record
def update_exam_record(student_records,student, exam):
    print("Updating", exam, "for student", student.upper())
    score = input("Enter the score for " + exam + ": ")

    while score.isdigit() == False:
        score = input("Enter the score for", exam)

    score = int(score)
    student_records[student][exam] = score

    save_to_file(student_records)

    list_student_scores(student_records,student)

    return_to_main()

# Display a list of students, with or without the exam records
def list_students(student_records, include_exam = False):

    for student_no, student_info in student_records.items():
        print("(", student_no, ") -", student_info["name"])
        if include_exam:
            print("Exam 1:", student_info["exam_1"])
            print("Exam 2:", student_info["exam_2"])
            print("Exam 3:", student_info["exam_3"])
            print("Exam 4:", student_info["exam_4"])
            print()

# Display a list of exam scores for a particular student
def list_student_scores(student_records, student_number):
    for i in range (1, 5):
        print("Exam "+ str(i) + ":", str(student_records[student_number]["exam_" + str(i)]))

# Save data to file
def save_to_file(student_records):
    with open(STUDENT_RECORD_FILE, "w") as student_file:
        json.dump(student_records, student_file) 

# Load saved student records from file
def load_from_file(file_name):   
    with open(file_name) as json_file:
        records = json.load(json_file)

    return records

# The main menu
def main_menu():
    selected_option = ''
    print("*** MAIN MENU ***")
    print()
    print("Please select from one of the following options:")
    print("1. List All Students Records")
    print("2. Update Student Record")
    print("3. Quit")
    print()

    while selected_option not in ["1", "2", "3"]:
        selected_option = input("Select an option: ")

    return selected_option

def header():
    print("STUDENT EXAM RECORD TRACKER")


if __name__ == '__main__':
    main()
