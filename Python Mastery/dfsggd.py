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
                    current_id = line.split("|")[0].split(":")[1].strip()

                    if book_ID == current_id:
                        found = True
                        break

        except FileNotFoundError:
            pass

        if found:
            print("Book ID already exists")

        else:
            info = (
                f"Book ID: {book_ID} | "
                f"Book name: {book_name} | "
                f"Aurthor name: {book_author} | "
                f"Book copies: {book_copies}\n"
            )

            with open("library management.txt", "a") as f:
                f.write(info)

            print("Book added successfully")


manager = LibraryManagement()
manager.add_book()
