students = {
    "Ankit": "A",
    "Harsh": "B"
}

while True:

    print("\n1. Add Student")
    print("2. Update Student Grade")
    print("3. Print all student Grades")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your Name: ")
        grade = input("Enter your grade: ")

        if name in students:
            print("Student already exists")
        else:
            students[name] = grade
            print("Student added successfully.....")

    elif choice == 2:
        name = input("Enter your Name: ")

        if name in students:
            grade = input("Enter your grade: ")
            students[name] = grade
            print("Grade updated successfully.....")
        else:
            print("Student not found")

    elif choice == 3:
        print("\nStudent grades:")

        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")