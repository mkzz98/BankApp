from account import Account
from customer import Customer

class Datasource:
    
    def getall(self):
        with open('BankInfo.txt', mode='rt') as file:
            temp = file.read()
            data_as_string = temp.split("\n")
            customers = []
        if not data_as_string[-1]:
            data_as_string.pop()
        for line in data_as_string:
            accounts = []
            first_split = line.split("#")
            for index, second_split in enumerate(first_split):
                element = second_split.split(":")
                if index == 0:
                    customer_id = element[0]
                    name = element[1]
                    pnr = element[2]
                else:
                    accountId = element[0]
                    accountType = element[1]
                    balance = element[2]
                    accounts.append(Account(accountId, accountType, balance))
            customers.append(Customer(customer_id, name, pnr, accounts))
        return customers
        

    def ToFile(self, info):
        with open("BankInfo.txt", "wt") as file:
            Inserttext = ""
            for customer in info:
                Inserttext += f"{customer.get_customer_id()}:{customer.get_name()}:" \
                                f"{customer.get_pnr()}"
                for account in customer.get_account():
                    Inserttext += f"#{account.get_accountId()}:{account.get_account_type()}" \
                                    f":{account.get_account_balance()} "
                Inserttext += "\n"
            file.write(Inserttext)

    def getnew(self):
        list_id = []
        with open("BankInfo.txt", mode="rt") as file:
            for line in file:
                string_split = line.strip().split(":")
                list_id.append(string_split[0])
                last_id = list_id[-1]
        return last_id

    def newaccountnumber(self):
        list_id = []
        with open("BankInfo.txt", mode="rt") as file:
            for line in file:
                first_split = line.strip().split("#")
                for index, middlehand in enumerate(first_split):
                    if not index == 0:
                        account_elements = middlehand.split(":")
                        list_id.append(account_elements[0])
        return max(list_id)

                
