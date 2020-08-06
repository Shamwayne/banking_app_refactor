# import pickle
# import os
# import pathlib
from enum import Enum


class AccountType(Enum):
    """Bank account types."""
    Current = "C"
    Savings = "S"


class Account(object):
    """Bank Account which stores data for a single account holder.

    Attributes:
        account_number: the unique account id issued by the bank
        name: the full name of the account holder
        balance: the amount of money stored in the account
        type: the account type, can be Savings or Current Account
    """
    account_number: int
    name: str
    _balance: int
    type: AccountType

    @property
    def balance(self):
        """Making the Account balance read only.

        This is to only have the deposit() and withdraw() methods to directly
        modify the balance of the bank account.
        """
        return self._balance

    def display(self):
        """Displays the formatted Account information onto the console."""
        display = f"""
        Account Number: {self.account_number}
        Account Holder Name: {self.name}
        Type of Account: {self.type}
        Balance: {self.balance}
        """
        print(display)

    def deposit(self, amount: int) -> None:
        """Deposits money into the bank account balance."""
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount cannot be less than zero!")

    def withdraw(self, amount: int) -> None:
        """Withdraws money from the bank account balance."""
        if (amount > 0) and (amount < self.balance):
            self._balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount!")

    def report(self):
        """Returns a TSV style report"""
        return f"{self.account_number}\t{self.name}\t{self.type}\t{self.balance}"


class AccountManager:
    """This class is to manage Account details.

    The createAccount, showAccount and modifyAccount methods that were 
    previously defined in the Accounts class are now going to be defined
    here.
    """
    pass