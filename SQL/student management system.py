import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_management_db"
    )

    cursor = conn.cursor()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")

            cursor.execute(
                "INSERT INTO student VALUES (%s,%s,%s,%s)",
                (student_id, name, age, course)
            )

            conn.commit()

            if cursor.rowcount > 0:
                print("Student Added Successfully")

        elif choice == 2:
            cursor.execute("SELECT * FROM student")
            students = cursor.fetchall()

            if students:
                for student in students:
                    print(student)
            else:
                print("No Student Found")

        elif choice == 3:
            student_id = int(input("Enter Student ID: "))

            cursor.execute(
                "SELECT * FROM student WHERE id=%s",
                (student_id,)
            )

            student = cursor.fetchone()
  
            if student:
                print(student)
            else:
                print("Student Not Found")

        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            course = input("Enter New Course: ")

            cursor.execute(
                "UPDATE student SET name=%s, age=%s, course=%s WHERE id=%s",
                (name, age, course, student_id)
            )

            conn.commit()

            if cursor.rowcount > 0:
                print("Student Updated Successfully")
            else:
                print("Student ID Not Found")

        elif choice == 5:
            student_id = int(input("Enter Student ID: "))

            cursor.execute(
                "DELETE FROM student WHERE id=%s",
                (student_id,)
            )

            conn.commit()

            if cursor.rowcount > 0:
                print("Student Deleted Successfully")
            else:
                print("Student ID Not Found")

        elif choice == 6:
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

except ValueError:
    print("Please enter only numbers where numbers are required.")

except mysql.connector.Error as e:
    print("MySQL Error:", e)

except Exception as e:
    print("Error:", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Database Connection Closed.")