from account import Account


class Customer:
    def __init__(self, customer_id, name, pnr, accounts):
        self.customer_id= customer_id
        self.name = name
        self.pnr = pnr
        self.accounts= accounts

    def __str__(self):
        return f"Customer ID: {self.customer_id} Name: {self.name} - Pnr: {self.pnr}"
    
    def get_customer_id(self):
        return self.customer_id
    def get_name(self):
        return self.name
    def get_pnr(self):
        return self.pnr
    def get_account(self):
        return self.accounts
    def set_name(self, name):
        self.name = name