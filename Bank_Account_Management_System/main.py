import csv
import os

class BankAccount:
    def __init__(self,account_number,name,balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = float(balance)
    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }
    def __str__(self):
        return f"Account_number: {self.account_number}, Name:{self.name}, Balance:{self.balance}"
class NewAccount():
    def __init__(self,filepath='users.csv'):
        self.filepath = filepath
        self.users = []
        self.read_file()

    def read_file(self):
        if os.path.exists(self.filepath):
            try:
                with open (self.filepath,'r',newline='') as csv_file:
                    reader = csv.DictReader(csv_file)
                    for row in reader:
                        bank_account = BankAccount(row['account_number'],row['name'],row['balance'])
                        self.users.append(bank_account)
            except Exception as e:
                print(f"Error reading file: {e}")
        else:
            print(f"File {self.filepath} not found. "
                  f"starting with an empty list")
    def write_file(self):
        try:
            with open(self.filepath,'w',newline='') as csvfile:
                fieldnames = ["account_number","name","balance"]
                writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
                writer.writeheader()
                account_numbers_written = set()
                for user in self.users:
                    if user.account_number not in account_numbers_written:
                        writer.writerow(user.to_dict())
                        account_numbers_written.add(user.account_number)
        except Exception as e:
            print(f"Error writing file: {e}")
    def create_account(self,account_number,name,balance=0):
        existing_user = self.find_user(account_number)
        if existing_user:
            existing_user.name = name
            existing_user.balance = balance
            self.write_file()
        else:
            new_user = BankAccount(account_number,name,balance)
            self.users.append(new_user)
            self.write_file()
    def find_user(self,account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None



    def deposit(self,account_number,amount):
        self.amount = amount
        user = self.find_user(account_number)
        if user:
            user.balance = user.balance + self.amount
            self.write_file()
            return f"You have deposited {self.amount} and your current balance is {user.balance}"
        else:
            return f"Invalid Credentials"

    def withdraw(self,account_number,amount):
        self.amount = amount
        user = self.find_user(account_number)
        if user:
            if self.amount <= user.balance:
                user.balance = user.balance - self.amount
                self.write_file()
                return f"You have withdrawn {self.amount} and your current balance is {user.balance}"
            else:
                return f"Insufficient funds!"
        else:
            return f"Invalid User"

    def check_balance(self,account_number):
        user = self.find_user(account_number)
        if user:
            return f"Your current balance is {user.balance}"
        else:
            return f"Account not found"


user3 = NewAccount()
user3.create_account(103,"potti",0)
user3.deposit(103,800)
user3.withdraw(103,100)
print(user3.withdraw(102,3000))

user4 = NewAccount()
user4.create_account(104,"sahithi",0)
user4.deposit(104,1000)
print(user4.withdraw(104,1200))
print(user4.withdraw(104,200))






