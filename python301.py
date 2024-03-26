# Create a banking app - Class based
# Actions: Withdrawal and Deposit
#          Write the transaction to a python file
# Must include: input, classes, open(), method, and properties

# Step 1: Create a class
class Bank:
    
    # Initialize the amount of money in the bank account
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount
    
    # Log the transactions
    def log_transaction(self, transaction_string):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string} \t\t\tBalance: {self.balance}\n")
    
    # Function for withdrawal and updates the balance.
    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.balance = self.balance - amount
        self.log_transaction(f"Withdrew ${amount}")
    
    # Function for deposit and updates the balance.
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.balance = self.balance + amount
        self.log_transaction(f"Deposit ${amount}")
    
    # Allows the user to print the balance in a proper format.
    def get_balance(self):
        return self.balance

# Variable for the class so we can use it.
account = Bank(0)

# Use a while loop.
while True:
    
    # Create a try and except condition so we can execute the code without dealing with the errors listed below.
    try:
        action = input("Would you like to make a deposit or withdrawal? ").lower()
    except KeyboardInterrupt:
        print("\nLeaving the ATM\n")
        break
    if action in ['withdrawal','deposit']:
        if action == 'deposit':
            amount = input("How much money would you like to put in?")
            account.deposit(amount)
        else:
            amount = input("How much money would you like to put in?")
            account.withdrawal(amount)
        print(f"Your current balance is {account.get_balance()}")
        
    else:
        print("That is not a valid action. Try again")

