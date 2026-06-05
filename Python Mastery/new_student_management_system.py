while True:
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Print number between 1 to 6 only")
        continue

    if choice == 1:
        student_name = input("Enter student name: ")
        student_age = int(input("Enter student age: "))
        student_subject = input("Enter student subject: ")
        student_marks = int(input("Enter student marks: "))
        info = f"Name: {student_name} | Age: {student_age} | Subject: {student_subject} | Marks: {student_marks}\n"

        with open("student management data.txt", "a") as f:
            f.write(info)

    elif choice == 2:
        with open("student management data.txt", "r") as f:
            print(f.read().strip())

    elif choice == 3:
        student_naam = input("Enter student name to search: ")
        found = False
        with open("student management data.txt", "r") as f:
            for line in f:
                if student_naam in line:
                    print(line)
                    break
        if not found:
            print("Student not found")

    elif choice == 4:
        student_naam = input("Enter student name to update: ")
        updated_line = []
        found = False
        with open("student management data.txt", "r") as f:
            for line in f:
                if f"Name: {student_naam}" in line:
                    print("Update student data")
                    update_age = int(input("Update age: "))
                    update_subject = input("Update subject: ")
                    update_marks = int(input("Update marks: "))
                    new_line = f"Name: {student_naam} | Age: {update_age} | Subject: {update_subject} | Marks: {update_marks}\n"
                    updated_line.append(new_line)
                    found = True
                else:
                    updated_line.append(line)
        if found:
            with open("student management data.txt", "w") as f:
                f.writelines(updated_line)
                print("Student updated successfully")
        else:
            print("Student not found")

    elif choice == 5:
        student_naam = input("Enter student name to delete: ")
        updated_line = []
        found = False
        with open("student management data.txt", "r") as f:
            for line in f:
                if student_naam in line:
                    found = True
                    break
                updated_line.append(line)
        if found:
            with open("student management data.txt", "w") as f:
                f.writelines(updated_line)

            print("Student deleted")
        else:
            print("Student not found")

    elif choice == 6:
        print("Goodbye!")
        break
