class Category:
  """
    Initializer
  """
  def __init__(self, name):
    self._name = name
    self.ledger = []

  """
    Adds amount to ledger
  """
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
  
  """
    Removes amount from ledger if enough funds (True), else do nothing (False)
  """
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
  
  """
    Returns total balance in ledger (deposits minus withdrawals)
  """
  def get_balance(self):
    bal = 0
    for entry in self.ledger:
      bal += entry["amount"]
    return bal

  """
    Transfers amount from one category to another if enough funds (True), else do nothin (False)
  """
  def transfer(self, amount, destination):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": "Transfer to {}".format(destination._name)})
      destination.ledger.append({"amount": amount, "description": "Transfer from {}".format(self._name)})
      return True
    else:
      return False
    
    return None

  """
    Checks if there are more funds in the ledger than a given amount
  """
  def check_funds(self, amount):
    if amount <= self.get_balance():
      return True
    else:
      return False
  
  """
    Builds standard string output when object is printed
  """
  def __str__(self):
    builder = ""
    astericks = (30 - len(self._name)) // 2
    builder += astericks*'*' + self._name + astericks*'*' + "\n"
    
    for entry in self.ledger:
      amount_len = len("{:.2f}".format(entry["amount"]))
      descr_len = len(entry["description"])
      if descr_len > 23:
        builder += entry["description"][:23] + " "*(7-amount_len) + "{:.2f}\n".format(entry["amount"])
      else:
        builder += entry["description"] + " "*(23-descr_len) + " "*(7-amount_len) + "{:.2f}\n".format(entry["amount"])
    
    builder += "Total: {:.2f}".format(self.get_balance())

    return builder

"""
    Creates bar chart to display spending percentages
"""
def create_spend_chart(categories):
  # get total spent withdrawn in each category and keep track of category with longest name
  spent_cat = [0,0,0]
  max_name_len = 0
  for i, cat in enumerate(categories):
    for entry in cat.ledger:
      if entry["amount"] < 0:
        spent_cat[i] += -entry["amount"]
    if max_name_len < len(cat._name):
      max_name_len = len(cat._name)
  
  total_spent = sum(spent_cat)
  percentages = [(cat / total_spent)*100 // 10 * 10 for cat in spent_cat]

  chart = "Percentage spent by category\n"
  
  # prints bulk of bar chart - prints 'o' when spending is more or equal to each axis label
  count_down = 100
  while count_down >= 0:
    chart += " "*(3-len(str(count_down))) + str(count_down) + "| "
    for perc in percentages:
      if perc >= count_down:
        chart += "o  "
      else:
        chart += 3*" "
    chart += "\n"
    count_down -= 10

  chart += 4*" " + "-"*(3*len(categories)+1) + "\n"

  # prints category names vertically
  cat_names = [list(cat._name) for cat in categories]
  for i in range(max_name_len):
    chart += 5*" "
    for cat in cat_names:
      if i < len(cat):
        chart += cat[i] + " "*2
      else:
        chart += " "*3
    if i+1 < max_name_len:
      chart += "\n"

  return chart