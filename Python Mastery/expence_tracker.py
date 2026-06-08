class ExpenseTracker:

    def add_expense(self):
        try:
            
            expence_name = input("Enter choice name: ")
            
            if not expence_name:
                print("Expanse name can't be empty")
                return
            
            expense=int(input("Enter expense amount: "))
            
            if expense<0:
                print("Expense cannot be negative")
                return
            
            info=f"Expense name: {expence_name} | Expense: {expense}\n"
            
            with open ("expense tracker.txt","a") as f:
                f.write(info)
            print("Expense added successfully")
            
        except ValueError:
            print("Try again")
        
    def view_expense(self):
        try:
            with open ("expense tracker.txt", "r") as f:
                data=f.read()
            if data:
                print(data)
            else:
                print("Data not found")
        except FileNotFoundError:
            print("File does not exixt")
            
    def total_expense(self):
        total=0
        try:
            with open("expense tracker.txt","r") as f:
                for line in f:
                    pages=line.split("|")
                    copies=int(pages[1].split(":")[1].strip())
                    
                    total+= copies
                    
                print(f"Total Expence= {total}")
        except FileNotFoundError:
            print("File does not exist")
    
    def delete_expense(self):
        expense_naam=input("Enter expense name to delete: ")
        updated_line=[]
        found=False
        try:
            with open("expense tracker.txt","r") as f:
                for line in f:
                    if expense_naam in line:
                        found=True
                        continue
                    updated_line.append(line)
            if found:
                with open ("expense tracker.txt","w") as f:
                    f.writelines(updated_line)
                print("Expense item deletes successfully")
            else:
                print("Expense item not found")
        except FileNotFoundError:
            print("File does not exist")
                        

manager=ExpenseTracker()
while True:
    print("1. Add expence")
    print("2. View expence")
    print("3. Total expence")
    print("4. Delete expence")
    print("5. Exit")
    
    try:
        choice=int(input("Enter choice(1-5): "))
        
        if choice == 1:
            manager.add_expense()

        elif choice == 2:
            manager.view_expense()

        elif choice == 3:
            manager.total_expense()

        elif choice == 4:
            manager.delete_expense()
            
        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice")
            
    except ValueError:
        print("Please enter valid number")


                    