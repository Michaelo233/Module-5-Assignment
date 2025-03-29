"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

__author__ = "COMP-1327 Faculty"
__version__ = "1.0.2025"
import unittest
from unittest import TestCase, main
from unittest.mock import patch
from src.chatbot import ACCOUNTS, VALID_TASKS
from src.chatbot import get_account_number, get_amount, get_balance

class Testchatbot(unittest.TestCase):
# test if the get account number raises a typeerror.
    def test_get_account_number_raise_type_error(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["knmskmdn"]
            expected = "Account number must be an int type."

            # Act
            with self.assertRaises(TypeError) as context:
                get_account_number()

            # Assert
            self.assertEqual(expected, str(context.exception))
            
# test if get account number raises a valueerror if account don't exist.
    def test_get_account_number_raise_value_error(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["123654"]
            expected = "Account number entered does not exist."

            # Act
            with self.assertRaises(ValueError) as context:
                get_account_number()

            # Assert
            self.assertEqual(expected, str(context.exception))
# test if get account number returns a valid account number.
    def test_get_account_number(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["123456"]
            expected = 123456

            # Act
            actual = get_account_number()

            # Assert
            self.assertEqual(expected, actual)

# test if get amount raises typeerror          
    def test_get_amount_raise_type_error(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["knmsk"]
            expected = "Amount must be a numeric type."

            # Act
            with self.assertRaises(TypeError) as context:
                get_amount()

            # Assert
            self.assertEqual(expected, str(context.exception))

# test if amount is equal to 0 and raise valueerror.  
    def test_get_amount_raise_value_error(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["0"]
            expected = "Amount must be a value greater than zero."

            # Act
            with self.assertRaises(ValueError) as context:
                get_amount()

            # Assert
            self.assertEqual(expected, str(context.exception))

# test if amount is less than 0 and raise a valueerror
    def test_get_amount_raise_value_error(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["-4444"]
            expected = "Amount must be a value greater than zero."

            # Act
            with self.assertRaises(ValueError) as context:
                get_amount()

            # Assert
            self.assertEqual(expected, str(context.exception))

# test if get_amount returns a valid amount.
    def test_get_amount(self):
        with patch('builtins.input') as mock_input:
            # Arrange
            mock_input.side_effect = ["1234"]
            expected = 1234

            # Act
            actual = get_amount()

            # Assert
            self.assertEqual(expected, actual)

# test if the get account number raises a typeerror.
    def test_get_balance_raise_type_error(self):
        # Arrange
        account_num = "aaaa"
        expected = "Account number must be an int type."

        # Act
        with self.assertRaises(TypeError) as context:
            get_balance(account_num)

        # Assert
        self.assertEqual(expected, str(context.exception))
            
# test if get balance raises a valueerror if account don't exist.
    def test_get_balance_raise_value_error(self):
        # Arrange
        account_num = 123487
        expected = "Account number does not exist."

        # Act
        with self.assertRaises(ValueError) as context:
            get_balance(account_num)

        # Assert
        self.assertEqual(expected, str(context.exception))
# test if get account number returns a valid account number.
    def test_get_balance(self):

        # Arrange
        account_num = 123456
        expected = f"Your current balance for account 123456 is $1,000.00."

        # Act
        actual = get_balance(account_num)

        # Assert
        self.assertEqual(expected, actual)