"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "COMP-1327 Faculty"
__version__ = "1.0.2025"

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

# Get account number function
def get_account_number() -> int:
    """
    This function asks the user for an input(account number)

    Arg:
    they user input is changed to an Int.

    Return:
    the account number is returned as an integer.
    """
    try:
        account_num = int(input("please enter your account number: "))
    except ValueError:
        raise TypeError("Account number must be an int type.")

    if account_num not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
    
    return account_num

# Get amount function.
def get_amount() -> float:
    try:
        input_amount = float(input("Enter an amount: "))
    except ValueError:
        raise TypeError("Amount must be a numeric type.")
    if input_amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
        
    return input_amount

# Get balance function.
def get_balance(account_num: int):
    try:
        account_num = int(account_num)
    except ValueError:
        raise TypeError("Account number must be an int type.")
    if account_num not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    else:
        account_balance = ACCOUNTS[account_num]["balance"]
        message = f"Your current balance for account {account_num} is ${account_balance:,.2f}."
        
    return message

# Make deposit function.

def make_deposit(account_num: int, amount: float) -> str:
    try:
        account_num = int(account_num)
    except ValueError:
        raise TypeError("Account number must be an int type.")
    try:
        amount = int(float(amount))
    except ValueError:
        raise ValueError("Amount must be a numeric type.")
    
    if account_num not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    
    else:
        message = f"You have made a deposit of ${amount:,.2f} to account {account_num}."
        ACCOUNTS[account_num]["balance"] += amount

    return message

# get tast function.
def get_task():
    account_option = input("What would you like to do (balance/deposit/exit)?: ").lower()
    if account_option not in VALID_TASKS:
        raise ValueError(f'"{account_option}" is an unknown task')
    
    return account_option

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

if __name__ == "__main__":
    chatbot()
