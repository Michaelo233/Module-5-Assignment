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

def get_amount():
    try:
        input_amount = float(input("Enter an amount: "))
    except ValueError:
        raise TypeError("Amount must be a numeric type.")
    if input_amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
        
    return input_amount

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
