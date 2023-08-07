# Attendance Management System - main.py

# Global variables
user_database = {}
student_database = {}
attendance_records = {}

# Task 1: User Authentication
def register_user(username, password):
    if username in user_database:
        return "Username already exists. Please choose a different username."
    user_database[username] = password
    return "Registration successful. You can now log in."

def login_user(username, password):
    if username not in user_database or user_database[username] != password:
        return "Invalid username or password. Please try again."
    return "Login successful."

# Task 2: Student Information Management6
def add_student(student_id, name):
    if student_id in student_database:
        return "Student ID already e…
[09:58, 31/07/2023] 💫🐍 Singh PIET: admin_database=("Shyam1", "Shyam2")
user_database = {}
student_database = {}

# User Authentication
def register_user(username, password):
    if username in user_database:
        return "Username already exists."
    user_database[username] = password
    return "Registration successful."

def login_user(username, password):
    if username not in user_database or user_database[username] != password:
        return "Invalid username or password."
    return "Login successful."

# Student Information Management
def add_student(student_id, name):
    if student_id in student_database:
        return "Student ID already exists."
    student_database[student_id] = name
    return "Student added successfully."

def view_students():
    return student_database

def update_student(student_id, new_name):
    if student_id not in student_database:
        return "Student ID not found."
    student_database[student_id] = new_name
    return "Student information updated successfully."

def delete_student(student_id):
    if student_id not in student_database:
        return "Student ID not found."
    del student_database[student_id]
    return "Student deleted successfully."

# Marking Attendance
def mark_attendance(date, student_ids_present):
    attendance_record = {}
    for student_id in student_ids_present:
        if student_id in student_database:
            attendance_record[student_id] = student_database[student_id]
    return attendance_record

def main():
    print("Welcome to the Attendance Management System")
    while True:
        print("\nOptions:")
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            message = register_user(username, password)
            print(message)

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            message = login_user(username, password)
            print(message)

            if message == "Login successful.":
                while True:
                    print("\nOptions:")
                    print("1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Mark Attendance\n6. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        student_id = input("Enter the Student ID: ")
                        name = input("Enter the Student's Name: ")
                        message = add_student(student_id, name)
                        print(message)

                    elif user_choice == "2":
                        students = view_students()
                        print("Students in the database:")
                        for student_id, name in students.items():
                            print(f"Student ID: {student_id}, Name: {name}")

                    elif user_choice == "3":
                        student_id = input("Enter the Student ID to update: ")
                        new_name = input("Enter the new Name: ")
                        message = update_student(student_id, new_name)
                        print(message)

                    elif user_choice == "4":
                        student_id = input("Enter the Student ID to delete: ")
                        message = delete_student(student_id)
                        print(message)

                    elif user_choice == "5":
                        date = input("Enter the date (YYYY-MM-DD): ")
                        student_ids_present = input("Enter Student IDs present").split(",")
                        attendance_record = mark_attendance(date, student_ids_present)
                        print("Attendance marked for:")
                        for student_id, name in attendance_record.items():
                            print(f"Student ID: {student_id}, Name: {name}")

                    elif user_choice == "6":
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exiting the Attendance Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()