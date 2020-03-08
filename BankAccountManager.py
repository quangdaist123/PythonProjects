# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:53:52 2020

@author: Lov
"""


class Account:
    # Hold universal attribute for a bank account
    def __init__(self, acc_num, opening_deposit):
        self.acc_num = acc_num
        self.balance = opening_deposit
        
    def __str__(self):
        return self.balance
        
    def deposit(self, amt):
        self.balance += amt
        
    def withdraw(self, amt):
        if amt > self.balance:
            print('Funds unavailable')
        else:
            self.balance -= amt


class Checking(Account):
    # for daily use
    def __init__(self, acc_num, opening_deposit):
        super().__init__(acc_num, opening_deposit)
        
    def __str__(self):
        # string representation
        return ('\tChecking account: {}\n\t\tBalance: {}'.format(self.acc_num, Account.__str__(self)))
        

class Savings(Account):
    # for long term
    def __init__(self, acc_num, opening_deposit):
        super().__init__(acc_num, opening_deposit)
    
    def __str__(self):
        # string representation
        return ('\tSavings account: {}\n\t\tBalance: {}'.format(self.acc_num, Account.__str__(self)))

        
class Business(Account):
    # for business management
    def __init__(self, acc_num, opening_deposit):
        super().__init__(acc_num, opening_deposit)
        
    def __str__(self):
        # string representation
        return ('\tBusiness account: {}\n\t\tBalance: {}'.format(self.acc_num, Account.__str__(self)))


class Customer():
    # for managing user account and perform various actions
    def __init__(self, username, name, PIN):
        self.username = username
        self.name = name
        self.PIN = PIN
        self.accts = {'C': [], 'S': [], 'B': []}
        
    def create_Checking(self, acc_num, opening_deposit):
        self.accts['C'].append(Checking(acc_num, opening_deposit))

    def create_Savings(self, acc_num, opening_deposit):
        self.accts['S'].append(Savings(acc_num, opening_deposit))
        
    def create_Business(self, acc_num, opening_deposit):
        self.accts['B'].append(Business(acc_num, opening_deposit))
        
    def get_total_deposit(self):
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance

        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
            
        print('\tTotal deposit:', total)
      
        
def make_dep(cust, acc_type, acc_num, amt):
    '''
    Parameters
    ----------
    cust : customer account.
    acc_type : type of bank accounts(C/S/B).
    acc_num : account numbers.
    amt : amount of money to deposit.

    Returns
    -------
    action DONE.
    '''
    for acct in cust.accts[acc_type]:
        if acct.acc_num == acc_num:
            acct.deposit(amt)


def make_wd(cust, acc_type, acc_num, amt):
    '''
    Parameters
    ----------
    cust : customer account.
    acc_type : type of bank accounts(C/S/B).
    acc_num : account numbers.
    amt : amount of money to withdraw.

    Returns
    -------
    action DONE.
    '''
    for acct in cust.accts[acc_type]:
        if acct.acc_num == acc_num:
            acct.withdraw(amt)


def create_Bank_acct(username):
    name = input('Enter your name: ')
    PIN = int(input('Enter your PIN: '))
    print('DONE')
    return Customer(username, name, PIN)


def choose_type_to_create(acct):
    print('\t 1. Checking')
    print('\t 2. Savings')
    print('\t 3. Business')
    option = int(input('Choose a type: '))
    number = int(input('Account number: '))
    amount = int(input('Amount of money: '))
    if option == 1:
        acct.create_Checking(number, amount)
    elif option == 2:
        acct.create_Savings(number, amount)
    elif option == 3:
        acct.create_Business(number, amount)
            

def print_info(acct):
    print('Username:', acct.username)
    print('Full name:', acct.name)
    acct.get_total_deposit()
                
    
def choose_type_to_adjust(acct, action):
    '''

    Parameters
    ----------
    acct: Pick a bank account
    action : Deposit or withdraw.

    Returns
    -------
    Action taken.

    '''
    print('\t 1. Checking')
    print('\t 2. Savings')
    print('\t 3. Business')
    option = int(input('Choose a type: '))
    number = int(input('Account number: '))
    amount = int(input('Amount of money: '))
    if option == 1:
        if action == 'deposit':
            make_dep(acct, 'C', number, amount)
        else:
            make_wd(acct, 'C', number, amount)
    elif option == 2:
        if action == 'deposit':
            make_dep(acct, 'S', number, amount)
        else:
            make_wd(acct, 'S', number, amount)
    elif option == 3:
        if action == 'deposit':
            make_dep(acct, 'B', number, amount)
        else:
            make_wd(acct, 'B', number, amount)


if __name__ == '__main__':
    # Finally I can get here :(
    option = ''
    accts_list = {}
    print('Welcome to my Bank Acount Management software\n')
    print('Choose an action:')
    print('1. Create a bank count')
    print('2. Check account information')
    print('3. Make deposit')
    print('4. Make withdraw')
    while option != 5:
        option = int(input('Your option: '))
        if option == 1:
            # Add a new username and use it to assign to a new Cust ojbect
            username = input('Enter acct username: ')
            # If a username already existed then skip the 'create' part
            if username not in accts_list:
                accts_list[username] = create_Bank_acct(username)
            # Pick a specific type of Bank account
            choose_type_to_create(accts_list[username])
            
        if option == 2:
            # Apply print_info function to all elements in accts_list
            list(map(print_info, accts_list.values()))
        
        if option == 3:
            username = input('Enter acct username: ')
            choose_type_to_adjust(accts_list[username], 'deposit')
            
        if option == 4:
            username = input('Enter your username')
            choose_type_to_adjust(accts_list[username], 'withdraw')
            
        if option == 5:
            print('Thank you for using')
            print("I've had a lot of fun doing this project")
