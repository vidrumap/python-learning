# main Account class to be inherited
class Account:
    def __init__(self,account_num,opening_deposit):
        self.account_num = account_num
        self.balance = opening_deposit

    def __str__(self):
        return f'${self.balance:.2f}'
    
    # accept deposits
    def deposit(self,amount):
        self.balance += amount

    # handle withdrawals
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print ('You do not have enough funds available to withdraw')

# creating different types of accounts based on Account class
class Checking(Account):
    def __init__(self, account_num, opening_deposit):
        super().__init__(account_num, opening_deposit)

    def __str__(self):
        return f'Checking Account #{self.account_num}\n  Balance: {Account.__str__(self)}'


class Savings(Account):
    def __init__(self, account_num, opening_deposit):
        super().__init__(account_num, opening_deposit)

    def __str__(self):
        return f'Savings Account #{self.account_num}\n  Balance: {Account.__str__(self)}'


class Business(Account):
    def __init__(self, account_num, opening_deposit):
        super().__init__(account_num, opening_deposit)

    def __str__(self):
        return f'Business Account #{self.account_num}\n  Balance: {Account.__str__(self)}'

# class to represent customer
class Customer:
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN
        self.accounts = {'C':[],'S':[],'B':[]}

    def __str__(self):
        return self.name
        
    def open_checking(self,account_num,opening_deposit):
        self.accounts['C'].append(Checking(account_num,opening_deposit))
    
    def open_savings(self,account_num,opening_deposit):
        self.accounts['S'].append(Savings(account_num,opening_deposit))
        
    def open_business(self,account_num,opening_deposit):
        self.accounts['B'].append(Business(account_num,opening_deposit))
        
    def get_total_deposits(self):
        total = 0
        for account in self.accounts['C']:
            print(account)
            total += account.balance
        for account in self.accounts['S']:
            print(account)
            total += account.balance
        for account in self.accounts['B']:
            print(account)
            total += account.balance
        print(f'Combined Deposits: ${total:.2f}') # added precision formatting here

def make_dep(customer,account_type,account_num,deposit_amount):
    for account in customer.accounts[account_type]:
        if account.account_num == account_num:
            account.deposit(deposit_amount)

def make_wd(customer,account_type,account_num,withdraw_amount):
    for account in customer.accounts[account_type]:
        if account.account_num == account_num:
            account.withdraw(withdraw_amount)
