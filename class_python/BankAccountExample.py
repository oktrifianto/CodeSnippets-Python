class BankAccount:
  def __init__(self, name):
    self.name    = name
    self.balance = 0          # init balance

  # add money
  def makeDeposit(self, amount):
    self.balance += amount
    return self.balance

  # withdraw money
  def makeWithdraw(self, amount):
    self.balance -= amount
    return self.balance

  # check amount 
  def getAmount(self):
    if self.balance == 0:
      return f'Sorry {self.name}, you don`t have money!'
    return f'Hi {self.name}, your money is ${self.balance}'

if __name__ == "__main__":
  # create instances
  JohnBank = BankAccount("John")
  JohnBank.makeDeposit(101)
  print(JohnBank.getAmount()) # $101
  JohnBank.makeWithdraw(31)
  print(JohnBank.getAmount()) # $101 - $31 = $70

  print("-----------------")
  JennieBank = BankAccount("Jennie")
  print(JennieBank.getAmount())   # $0 --- don't have money
  JennieBank.makeDeposit(45)
  print(JennieBank.getAmount())




  