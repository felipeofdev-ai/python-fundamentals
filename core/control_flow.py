"""
Module: control_flow
Author: Felipe Fernandes

Examples of conditional statements and loops,
focused on readability, correctness, and clean logic.
"""

from typing import Iterable


def is_even(number: int) -> bool:
    """
    Check if a number is even.

    Args:
        number: Integer to be evaluated

    Returns:
        True if the number is even, False otherwise
    """
    return number % 2 == 0


def categorize_number(number: int) -> str:
    """
    Categorize a number based on its value.

    Args:
        number: Integer to be categorized

    Returns:
        A string describing the number category
    """
    if number < 0:
        return "negative"
    if number == 0:
        return "zero"
    return "positive"


def filter_even_numbers(numbers: Iterable[int]) -> list[int]:
    """
    Filter even numbers from an iterable.

    Args:
        numbers: Iterable of integers

    Returns:
        A list containing only even numbers
    """
    return [n for n in numbers if is_even(n)]


def sum_until_limit(numbers: Iterable[int], limit: int) -> int:
    """
    Sum numbers until a limit is reached.

    Stops processing once the accumulated sum
    exceeds the provided limit.

    Args:
        numbers: Iterable of integers
        limit: Maximum allowed sum

    Returns:
        The accumulated sum
    """
    total = 0

    for number in numbers:
        total += number
        if total > limit:
            break

    return total
