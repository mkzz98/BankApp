class Account:
    
    def __init__(self, accountId, accountType, balance):
        self.balance= float(balance)
        self.accountId= accountId
        self.accountType= accountType
        
    def __str__(self):
        return f"Account ID: {self.accountId},  Account type: {self.accountType}, Balance: {self.balance}"  
     
    def get_accountId(self):
        return self.accountId
    def get_account_type(self):
        return self.accountType
    def get_account_balance(self):
        return self.balance
    def set_balance(self, new_balance):
        self.balance = new_balance 