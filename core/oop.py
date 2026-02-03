"""
Module: oop
Author: Felipe Fernandes

Basic object-oriented programming examples in Python,
focused on clean design, encapsulation, and responsibility.
"""


class BankAccount:
    """
    Simple bank account model demonstrating encapsulation
    and behavior-driven design.
    """

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        """Return the current account balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """
        Deposit a positive amount into the account.

        Args:
            amount: Amount to deposit

        Raises:
            ValueError: If the amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw an amount from the account if sufficient balance exists.

        Args:
            amount: Amount to withdraw

        Returns:
            True if the withdrawal was successful, False otherwise
        """
        if amount <= 0 or amount > self._balance:
            return False

        self._balance -= amount
        return True
