import json
import random

class Account:
  def __init__(self):
    self.filepath = "accountdata.json"
    self.account = str(random.randint(100000000000, 999999999999))
    self.pin_num = ""
    self.balance = 0

  def load(self):         #loads file
    with open(self.filepath) as f_object:
      data = json.load(f_object)
      return data

  def save(self, data):     #saves file
    with open(self.filepath, 'w') as f_object:
      json.dump(data, f_object, indent=2)

  def deposit(self):
      data = self.load()
      amount = input("Enter the amount you'd like to deposit")
      current_balance = float(data[self.account]["balance"])
      current_balance += float(amount)
      data[self.account]["balance"] = current_balance
      self.save(data)

  def withdraw(self):
        data = self.load()
        current_balance = float(data[self.account]["balance"])
        withdrawl = float(input("How much would you like to withdraw? "))
        if withdrawl > current_balance:
            current_balance = current_balance
            print("Error, you will overdraft your account!")
        else:
            current_balance -= withdrawl
        data[self.account]["balance"] = current_balance
        self.save(data)

  def balance(self):
      data = self.load()
      current_balance = self.account["balance"]
      print("Your account balance is: ", float(current_balance))
      print("-----------------------------------------------")
      print("_______________________________________________")



  def create_account(self):   #create account
    data = self.load()
    self.pin_num = input("Please enter a numerical pin number ")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    data[self.account]={"Account #": self.account, "balance": 0, "First_name":first_name, "Last_name": last_name, "pin_num": self.pin_num}
    option = input("Would you like to deposit $25? Y/N: ")
    if option.lower() == "y":
      data[self.account]={"Account": self.account, "balance": 25, "First_name": first_name, "Last_name": last_name, "pin_num": self.pin_num}
    self.save(data)

  def login_menu(self):
    data = self.load()               #When the user logs in, and is prompted what todo
    self.account = input('Enter Account #: ')
    self.pin_num = input("Please enter a numerical pin number ")
    # check if account number is numeric and in the json file
    if not self.account.isnumeric():
        print("Invalid input. Account Number must have numeric values")
        return
        if not self.pin_num.isnumeric():
            print("Invalid input. Pin # must have numeric values!")
            return
    if self.account in data and self.pin_num in data[self.account]["pin_num"]: #checks account num and pin number in data
        print("Please choose an option:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")
        option = input()
        while option not in ['1', '2', '3', '4']:
            option = input("Sorry, that's an invalid option! Please choose 1, 2 or 3: ")

        if option == '1':
            self.withdraw()   #since data = model.Account(). Switched model.withdraw(account) to data.withdraw(account)
        elif option == '2':
            self.deposit()
        elif option == '3':
            self.balance
        elif option == '4':
            return

  

    