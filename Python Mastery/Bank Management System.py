class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            print("Invalid amount")
            return False

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            print("Insufficient amount")
            return False

    def show_balance(self):
        print(f"Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance


class SavingAccount(BankAccount):

    def __init__(self, name, account_number, balance, interest):
        super().__init__(name, account_number, balance)
        self.interest = interest

    def show_interest(self):
        return self.get_balance() * self.interest // 100


class CurrentAccount(BankAccount):
    def __init__(self, name, account_number, balance, business_name):
        super().__init__(name, account_number, balance,)
        self.business_name = business_name


class AccountManagement:

    def save_account(self):
        name = input("Enter the name: ")
        account = int(input("Enter the account number: "))
        balance = int(input("Enter the balance: "))
        found = False
        try:
            with open("bank_details.txt", "r") as f:
                for line in f:
                    parts=[i.strip() for i in line.split("|")]
                    if parts[2]==str(account):
                        found = True
                        break

        except FileNotFoundError:
            pass

        if found:
            print("Account already exist")
        else:
            account_type = input("Enter account type: ")

            if account_type.lower() == "saving":
                interest = int(input("Enter the interest rate: "))
                obj = SavingAccount(name, account, balance, interest)
                data = (
                    f"Saving |"
                    f"{obj.name} |"
                    f"{obj.account_number} |"
                    f"{obj.get_balance()} |"
                    f"{obj.interest} \n"
                )
            else:
                business_name = input("Enter business name: ")
                obj = CurrentAccount(name, account, balance, business_name)
                data = (
                    f"Current |"
                    f"{obj.name} |"
                    f"{obj.account_number} |"
                    f"{obj.get_balance()} |"
                    f"{obj.business_name}\n"
                )
            with open("bank_details.txt", "a") as f:
                f.write(data)
            print("account created successfully")

    def login(self):
        account_number = int(input("Enter account number: "))
        found = False
        try:
            with open("bank_details.txt", "r") as f:
                for line in f:
                    parts=[i.strip() for i in line.split("|")]
                    if (parts[2]==str(account_number)):
                        found=True
                        if parts[0]=="Saving":
                            obj=SavingAccount(parts[1],int(parts[2]),int(parts[3]),int(parts[4]))
                        else:
                            obj=CurrentAccount(parts[1],int(parts[2]),int(parts[3]),parts[4])
                            
                        print("Login Succcessfully")
                        self.account_menu(obj)
                        break
                    
            if not found:
                print("account not found")
        except FileNotFoundError:
            print("File does not exist")          
            
            
            
    def account_menu(self, obj):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. logout")
            choice=int(input("Enter the choice: "))
            if choice == 1:
                amount=int(input("Enter the number to deposit: "))
                if obj.deposit(amount):
                    self.update_line(obj)
                    print("Deposited successfully")
                
            elif choice == 2:
                amount=int(input("Enter number to withdraw: "))
                if obj.withdraw(amount):
                    self.update_line(obj)
                    print("Withdraw successfully")
                
            elif choice == 3:
                obj.show_balance()
                
            elif choice == 4:
                print("Logged out")
                break
            else:
                print("Invalid choice")
                
    def update_line(self,obj):
        new_line=[]
        found=False
        try:
            with open("bank_details.txt","r") as f:
                for line in f:
                    parts=[i.strip() for i in line.split("|")]
                    if parts[2]==str(obj.account_number):
                        found=True
                        if parts[0]=="Saving":
                            updated_line=(
                                f"Saving |"
                                f"{obj.name} |"
                                f"{obj.account_number} |"
                                f"{obj.get_balance()} |"
                                f"{obj.interest}\n"
                            )
                        else:
                            updated_line=(
                                f"Current |"
                                f"{obj.name} |"
                                f"{obj.account_number} |"
                                f"{obj.get_balance()} |"
                                f"{obj.business_name}\n"
                            )
                            
                        new_line.append(updated_line)
                    else:
                        new_line.append(line)
                        
            with open("bank_details.txt","w") as f:
                f.writelines(new_line)
        except FileNotFoundError:
            print("File does not exixt")
            
            
    def delete_account(self):
        account=int(input("Enter the accounter number to delete: "))
        new_line=[]
        found=False
        try:
            with open("bank_details.txt","r") as f:
                for line in f:
                    parts=[i.strip() for i in line.split("|")] 
                    if parts[2]==str(account):
                        found=True
                        continue
                    new_line.append(line)
                if found:
                    with open("bank_details.txt","w") as f:
                        f.writelines(new_line)
                    print("Accound information deleted")
                else:
                    print("Account not found")
                    
        except FileNotFoundError:
            print("File does not exist")
                    
                                  
                
        
manager = AccountManagement()
while True:
    print("1. Create Account")
    print("2. Login")
    print("3. Delete Account")
    print("4. Exit")
    try:
        choice = int(input("Enter the choice: "))
        if choice == 1:
            manager.save_account()

        elif choice == 2:
            manager.login()

        elif choice == 3:
            manager.delete_account()
            
        elif choice == 4:
            print("Bye")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter number only")