class StudentManagement:

    def add_student(self):
        student_name = input("Enter student name: ")
        student_age = int(input("Enter student age: "))
        student_subject = input("Enter student subject: ")
        student_marks = int(input("Enter student marks: "))

        info = f"Name: {student_name} | Age: {student_age} | Subject: {student_subject} | Marks: {student_marks}\n"

        with open("student management.txt", "a") as f:
            f.write(info)
        print("Student added successfully")

    def view_student(self):
        try:
            with open("student management.txt", "r") as f:
                data = f.read()
            if data:
                print(data)
            else:
                print("No studentt record found")
        except FileNotFoundError:
            print("file does not exist")

    def search_student(self):
        student_naam = input("Enter student name to search: ")
        found = False
        try:
            with open("student management.txt", "r") as f:
                for line in f:
                    if student_naam.lower() in line.lower():
                        print(line)
                        found = True
            if not found:
                print("Student not found")
        except FileNotFoundError:
            print("File does not exist")

    def update_student(self):
        student_naam = input("Enter student name to update: ")
        updated_line = []
        found = False

        try:
            with open("student management.txt", "r") as f:
                for line in f:
                    if student_naam.lower() in line.lower():
                        update_age = int(input("Update age: "))
                        update_subject = input("Update subject: ")
                        update_marks = int(input("Update marks: "))
                        info = f"Name: {student_naam} | Age: {update_age} | Subject: {update_subject} | Marks: {update_marks}\n"

                        updated_line.append(info)
                        found = True

                    else:
                        updated_line.append(line)
            if found:
                with open("student management.txt", "w") as f:
                    f.writelines(updated_line)
                print("Updated Student data successfully")

            else:
                print("Student not found")

        except FileNotFoundError:
            print("File does not exixt")

    def delete_student(self):

        student_naam = input("Enter student name which you want to delete: ")
        updated_line = []
        found = False
        try:
            with open("student management.txt", "r") as f:
                for line in f:
                    if student_naam.lower() in line.lower():
                        found = True
                        continue
                    updated_line.append(line)
            if found:
                with open("student management.txt", "w") as f:
                    f.writelines(updated_line)
                print("Student data deleted")
            else:
                print("Student not found")
        except FileNotFoundError:
            print("File does not exist")


manager = StudentManagement()

while True:
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    try:
        choice = int(input("Enter choice(1-6): "))

        if choice == 1:
            manager.add_student()

        elif choice == 2:
            manager.view_student()

        elif choice == 3:
            manager.search_student()

        elif choice == 4:
            manager.update_student()

        elif choice == 5:
            manager.delete_student()

        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid number")
