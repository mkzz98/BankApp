from bank import Bank

class Menu:

    def __init__(self):
        self.bank = Bank()
        self.menu()

    def menu(self):
        print("Welcome to bank Bank")
        while True:
            print("1. Open Account")
            print("2. Change Name")
            print("3. Close Account")
            print("4. Close Customer")
            print("5. Withdraw Money")
            print("6. Deposit Money")
            print("7. Add Account")
            print("8. Show Accounts")
            print("9. Show Customer")
            print("10.Get Account")
            print("0. Exit")
            option = int(input())
            if option == 1:
                name = input("Enter your full name: ")
                pnr = input("Enter your SSN: ")
                self.bank.add_customer(name, pnr)
            elif option == 2:
                name = input("Enter your new name: ")
                pnr = input("Enter your SSN: ")       
                self.bank.change_name(name, pnr)
            elif option == 3:
                pnr = input("Enter your SSN: ")
                accountId = input("Enter your account number: ")
                self.bank.close_account(pnr, accountId)
            elif option == 4:
                pnr = input("Enter your SSN: ")
                self.bank.remove_customer(pnr)
            elif option == 5:
                pnr = input("Enter your SSN: ")
                accountId = input("Enter your account number: ")
                amount = input("Amount: ")
                self.bank.withdraw(pnr, accountId, amount)
            elif option == 6:
                pnr = input("Enter your SSN: ")
                accountId = input("Enter your account number: ")
                amount = input("Amount: ")
                self.bank.deposit(pnr, accountId, amount)
            elif option == 7:
                pnr = input("Please enter your SSN: ")
                self.bank.add_account(pnr)
            elif option == 8:
                self.bank.get_customers()
            elif option == 9:
                pnr = input('Enter your SSN: ')
                self.bank.get_customer(pnr)
            elif option == 10:
                pnr = input("Pnr: ")
                accountId = input("Account number: ")
                self.bank.get_account(pnr, accountId)
            elif option == 0:
                print("Thank you! Come again!")
                self.bank.exit()
            else:
                print("Please choose one of the available options")


if __name__ == "__main__":
    print("This python script is not meant to be run directly, please import in another class!")
    quit()