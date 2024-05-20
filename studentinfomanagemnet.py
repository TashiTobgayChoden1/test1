# Initialize empty lists and dictionary
students_list = []
students_dict = {}

# Function to add a new student
def add_student():
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grade = input("Enter the student's grade: ")

    # Add the student to the list and dictionary
    students_list.append(name)
    students_dict[name] = {"age": age, "grade": grade}

    print(f"Student {name} added successfully!")
    print("Student Details:")
    for name, details in students_dict.items():
        print(f"Name: {name}, Age: {details['age']}, Grade: {details['grade']}")
    print()

# Function to search for a student
def search_student():
    name = input("Enter the student's name to search: ")
    if name in students_dict:
        details = students_dict[name]
        print(f"Name: {name}, Age: {details['age']}, Grade: {details['grade']}")
    else:
        print(f"Student '{name}' not found.")
    print()

# Function to remove a student
def remove_student():
    name = input("Enter the student's name to remove: ")
    if name in students_dict:
        students_list.remove(name)
        del students_dict[name]
        print(f"Student '{name}' removed successfully.")
    else:
        print(f"Student '{name}' not found.")
    print()

# Main loop
while True:
    print("Student Information Management System")
    print("1. Add a new student")
    print("2. Search for a student")
    print("3. Remove a student")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    print()

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        print()
        