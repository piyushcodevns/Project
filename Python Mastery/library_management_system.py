class LibraryManagement:

    def add_book(self):
        book_ID = input("Enter book ID: ")
        book_name = input("Enter book name: ")
        book_author = input("Enter book author name: ")
        book_copies = int(input("Enter book copies: "))

        found = False
        try:
            with open("library management.txt", "r") as f:
                for line in f:
                    current_line = line.split("|")[0].split(":")[1].strip()
                    if book_ID == current_line:
                        found = True
                        break
        except FileNotFoundError:
            pass

        if found:
            print("Book ID already exist")
        else:
            info = (
                f"Book_ID: {book_ID} |"
                f"Book name: {book_name} |"
                f"Aurthor name: {book_author} |"
                f"Book copies: {book_copies}\n"
            )
            with open("library management.txt", "a") as f:
                f.write(info)
            print("Book added successfully")

    def view_book(self):
        try:
            with open("library management.txt", "r") as f:
                data = f.read()
            if data:
                print(data)
            else:
                print("Library data is empty")
        except FileNotFoundError:
            print("File does not exist")

    def search_book(self):
        book_ID = input("Enter book ID to find book: ")
        found = False
        try:
            with open("library management.txt", "r") as f:
                for line in f:
                    if book_ID in line:
                        print(line)
                        found = True
            if not found:
                print("Book info not found")
        except FileNotFoundError:
            print("File does not exist")

    def delete_book(self):
        book_ID = input("Enter book to delete info: ")
        updated_line = []
        found = False
        try:
            with open("library management.txt", "r") as f:
                for line in f:
                    if book_ID in line:
                        found = True
                        continue
                    updated_line.append(line)
            if found:
                with open("library management.txt", "w") as f:
                    f.writelines(updated_line)
                print("Book information deleted")
            else:
                print("Book info not found")
        except FileNotFoundError:
            print("File does not exist")

    def issue_book(self):
        book_ID = input("Enter book ID to issue: ")
        updated_line = []
        found = False
        try:
            with open("library management.txt", "r") as f:
                for line in f:
                    if book_ID in line:
                        found = True

                        pages = line.split("|")
                        copies = int(pages[3].split(":")[1])
                        if copies > 0:
                            copies -= 1
                            new_line = (
                                f"{pages[0]} |"
                                f"{pages[1]} |"
                                f"{pages[2]} |"
                                f"Book copies: {copies}\n"
                            )
                            updated_line.append(new_line)
                            print("Book issued successfully")
                        else:
                            updated_line.append(line)
                            print("Book not avaiable")
                    else:
                        updated_line.append(line)

            if found:
                with open("library management.txt", "w") as f:
                    f.writelines(updated_line)
            else:
                print("Book ID not found")
        except FileNotFoundError:
            print("File does not exist")

    def return_book(self):
        book_ID = input("Enter book ID to return: ")
        updated_line = []
        found = False
        try:
            with open("library management.txt", "r") as f:
                for line in f:
                    if book_ID in line:
                        found = True
                        pages = line.split("|")
                        copies = int(pages[3].split(":")[1])
                        copies += 1
                        new_line = (
                            f"{pages[0]} |"
                            f"{pages[1]} |"
                            f"{pages[2]} |"
                            f" Book copies: {copies}\n"
                        )
                        updated_line.append(new_line)
                        print("Book returne successfully")

                    else:
                        updated_line.append(line)
            if found:
                with open("library management.txt", "w") as f:
                    f.writelines(updated_line)
            else:
                print("Book Id not found")

        except FileNotFoundError:
            print("File does not exist")


manager = LibraryManagement()

while True:
    print("1. Add book")
    print("2. View book")
    print("3. Search book")
    print("4. Delete book")
    print("5. Issue book")
    print("6. Return book")
    print("7. Exit")

    try:
        choice = int(input("Enter choice(1-7): "))

        if choice == 1:
            manager.add_book()

        elif choice == 2:
            manager.view_book()

        elif choice == 3:
            manager.search_book()

        elif choice == 4:
            manager.delete_book()

        elif choice == 5:
            manager.issue_book()

        elif choice == 6:
            manager.return_book()

        elif choice == 7:
            print("Goodbye!")
            break

        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter valid number")
