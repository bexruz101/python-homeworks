import random

class Account:
  def __init__(self,name,initial_deposit):
    self.account_number = self.generate_account_number()
    self.name = name
    self.balance = initial_deposit

  def generate_account_number(self):
    return random.randint(10000,99999)

  def deposit(self,amount):
    self.balance+=amount

  def withdraw(self,amount):
    if self.balance >= amount:
      self.balance-=amount
    else:
      print("Insufficient funds!")

  def __str__(self):
    return f"Account Number: {self.account_number}\nName: {self.name}\nBalance: {self.balance}"


class Bank:
  def __init__(self):
    self.accounts = {}
  
  def create_account(self,name,initial_deposit):
    new_account = Account(name,initial_deposit)
    self.accounts[new_account.account_number] = new_account
    return new_account.account_number

  def view_account(self,account_number):
    if account_number in self.accounts:
      print(self.accounts[account_number])
    else:
      print("Account not found!")
  
  def deposit(self,account_number,amount):
    if account_number in self.accounts:
      self.accounts[account_number].deposit(amount)

  def withdraw(self,account_number,amount):
    if account_number in self.accounts:
      self.accounts[account_number].deposit(amount)
    
  def save_to_file(self):
    with open("accounts.txt","w") as file:
      for account_number,account in self.accounts.items():
        file.write(f"{account_number},{account.name},{account.balance}\n")
  
  def load_from_file(self):
    try:
      with open("accounts.txt","r") as file:
        for line in file:
          account_number,name,balance = line.strip().split(",")
          self.accounts[int(account_number)] = Account(name,float(balance))
    except FileNotFoundError:
      print("No previous account data found.")
if __name__ == "__main__":
    bank = Bank()

    # Example operations
    acc1 = bank.create_account("Alice", 1000)
    acc2 = bank.create_account("Bob", 500)

    bank.deposit(acc1, 500)
    bank.withdraw(acc2, 200)

    bank.view_account(acc1)
    bank.view_account(acc2)

    bank.save_to_file()
    bank.load_from_file()
  



    
  
