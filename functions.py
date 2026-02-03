"""
Module: functions
Author: Felipe Fernandes

This module contains core examples of Python functions,
demonstrating clean signatures, type hints, docstrings,
and basic error handling.

The goal is to show practical and readable function design.
"""

from typing import Optional


def add(a: int, b: int) -> int:
    """
    Return the sum of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Return the subtraction of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The result of a - b
    """
    return a - b


def divide(a: float, b: float) -> Optional[float]:
    """
    Divide two numbers safely.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        The division result, or None if division is not possible
    """
    if b == 0:
        return None
    return a / b


def average(*values: float) -> float:
    """
    Calculate the arithmetic mean of a variable number of values.

    Args:
        *values: A sequence of numeric values

    Returns:
        The arithmetic mean, or 0.0 if no values are provided
    """
    if not values:
        return 0.0
    return sum(values) / len(values)


def format_greeting(name: str, title: str = "Mr.") -> str:
    """
    Format a greeting message.

    Args:
        name: Person's name
        title: Optional title (default is 'Mr.')

    Returns:
        A formatted greeting string
    """
    return f"Hello, {title} {name}!"
