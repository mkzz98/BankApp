from customer import Customer
from account import Account
from datasource import Datasource


class Bank:
    
    def __init__(self):
        self.datasource = Datasource()
        self.info= []
        self._load()
        
 #Läser in text filen och befolkar listan som ska innehålla kunderna.
    def _load(self):
        self.info = self.datasource.getall()

#Returnerar bankens alla kunder (personnummer och namn)
    def get_customers(self):
        for customer in self.info:
            print(customer)
                          
#Skapar en ny kund med namn och personnummer.
# Kunden skapas endast om det inte finns någon kund med personnumret som angetts.
# Returnerar True om kunden skapades annars returneras False.
    def add_customer(self, name, pnr):
        for customer in self.info:
            if pnr == customer.get_pnr():
                print("Customer already exist!")
                return 
        else:
            last_id = int(self.datasource.getnew())
            last_id += 1
            new_customer = Customer(last_id, name, pnr, [])
            self.info.append(new_customer)
            self.datasource.ToFile(self.info)
            print("Customer creation successfull")
            return 
            
#Returnerar information om kunden inklusive dennes konton.
    def get_customer(self, pnr):
        for customer in self.info:
            if pnr ==  customer.get_pnr():
                for account in customer.get_account():
                    print(customer, account)
    
#Byter namn på kund, returnerar
# True om namnet ändrades annars returnerar det False(om kunden inte fanns).
    def change_name(self, name, pnr):
        for customer in self.info:
            if pnr == customer.get_pnr():
                customer.set_name(name)
                print("Name changed succefully to",customer.get_name())
                self.datasource.ToFile(self.info)
                return
        else:
            print("Sorry no account with that SSN exist!")
            return

            
#Tar bort kund med personnumret som angetts ur banken,
# alla kundens eventuella konton tas också bort och resultatet returneras.
    def remove_customer(self, pnr):
        for customer in self.info:
            if customer.get_pnr() == pnr:
                index = self.info.index(customer)
                for account in customer.get_account():
                    self.info.pop(index)
                    print("Customer with SSN:",customer.get_pnr(), "was successfully closed. Remaining balance will be returned:", account.get_account_balance())
                    self.datasource.ToFile(self.info)
                    return
        else:
            print("No customer with that SSN exist!")
            return
#Skapar ett konto till kunden med personnumret som angetts, returnerar kontonumret
# som det skapade kontot fick alternativt returneras –1 om inget konto skapades.
    def add_account(self,pnr):
        new_account = int(self.datasource.newaccountnumber())
        new_account += 1
        for customer in self.info:
            if customer.get_pnr() == pnr:
                new_account = Account(new_account, 'Debit', 0.0)
                customer.get_account().append(new_account)
                print("New account was added!")
                self.datasource.ToFile(self.info)
                return
        else:
            print("No person with that SSN exist")
            return
            

#Returnerar Textuell presentation
# av kontot med kontonummer som tillhör kunden (kontonummer, saldo, kontotyp).
    def get_account(self, pnr, accountId):
        for customer in self.info:
            if pnr == customer.get_pnr():
                for account in customer.get_account():
                    if accountId == account.get_accountId():
                        print(account)

#Gör en insättning på kontot, returnerar True om det gick bra annars False.
    def deposit(self, pnr, accountId, amount):
        for customer in self.info:
            if pnr == customer.get_pnr():
                for account in customer.get_account():
                   if accountId == account.get_accountId():
                        balance = account.get_account_balance()                        
                        balance += float(amount)
                        account.set_balance(balance)
                        print("Succefully deposited",amount,"Balance is now",account.get_account_balance())
                        self.datasource.ToFile(self.info)
                        return
        else:
            print("Sorry no person exist with that SSN!")
                

#Gör ett uttag på kontot, returnerar True om det gick bra annars False.
    def withdraw(self, pnr, accountId, amount):
        for customer in self.info:
            if pnr == customer.get_pnr():
                for account in customer.get_account():
                    if accountId == account.get_accountId():
                        if account.get_account_balance() >= float(amount):
                            balance = account.get_account_balance()
                            balance -= float(amount)
                            account.set_balance(balance)
                            print("Sucessfully withdrew",amount,"Remaining balance",account.get_account_balance())
                            self.datasource.ToFile(self.info)
                            return
                        else:
                            print("You are to poor/wrong account id")
                            return
        else:
            print("No customer with that SSN exist")
            return
#Avslutar ett konto.
    def close_account(self, pnr, accountId):
        for customer in self.info:
            if customer.get_pnr() == pnr:
                for account in customer.get_account():
                    index = customer.get_account().index(account)
                    if accountId == account.get_accountId():
                        customer.get_account().pop(index)
                        print("Account with account number: ",account.get_accountId(), "was successfully closed. Remaining balance will be returned: ", account.get_account_balance())
                        self.datasource.ToFile(self.info)
                        return
                    else:
                        print("This customer does not have a that account id")
                        return
        else:
            print("No person with that SSN exist")
            return

    def exit(self):
        quit()