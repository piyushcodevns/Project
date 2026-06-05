while True:
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete stuednt")
    print("6. Exit")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Only number allowed")
        continue

    # If you choice 1
    if choice == 1:
        student_name = input("Enter student name: ")
        student_age = int(input("Enter student age: "))
        student_subject = input("Enter student subject: ")
        student_marks = int(input("Enter student subject marks: "))
        with open("student_information.txt", "a") as f:
            f.write(
                f"Name: {student_name} | Age: {student_age} | Subject: {student_subject} | Marks: {student_marks}\n"
            )
        print("Student added successfully")

    # If you choice 2
    elif choice == 2:
        print("View Student")
        with open("student_information.txt", "r") as f:
            print(f.read().strip())

    # If you choice 3
    elif choice == 3:
        print("Search Student")
        search_student = input("Enter student name: ")
        found = False
        with open("student_information.txt", "r") as f:
            for line in f:
                if search_student in line:
                    print(line)
                    found = True
        if not found:
            print("Student not found")

    # If you choice 4
    elif choice == 4:
        print("Update Student")
        student_naam = input("Enter student name: ")
        updated_lines = []
        found = False
        with open("student_information.txt", "r") as f:
            for line in f:
                if f"Name: {student_naam}" in line:
                    update_age = input("Update student age: ")
                    update_subject = input("Update student subject: ")
                    update_marks = int(input("Update student marks: "))
                    new_line = f"Name: {student_naam} | Age: {update_age} | Subject: {update_subject} | Marks: {update_marks}\n"
                    updated_lines.append(new_line)
                    found = True
                else:
                    updated_lines.append(line)
        if found:
            with open("student_information.txt", "w") as f:
                f.writelines(updated_lines)
            print("Student Updated successfully")
        else:
            print("Student not found")

    # If you choice 5
    elif choice == 5:
        print("Delete student")
        student_naam = input("Enter student name: ")
        updated_lines = []
        found = False
        with open("student_information.txt", "r") as f:
            for line in f:
                if student_naam in line:
                    found = True
                    break
                updated_lines.append(line)

        if found:
            with open("student_information.txt", "w") as f:
                f.writelines(updated_lines)

            print("Student Deleted successfully")
        else:
            print("Student not found")
            
    elif choice == 6 :
        print("Goodbye!")
    break
