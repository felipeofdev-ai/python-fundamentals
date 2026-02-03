"""
Module: mini_challenges
Author: Felipe Fernandes

Small problem-solving challenges designed to demonstrate
logic, clarity, and clean Python fundamentals.
"""

from typing import Iterable


def find_max(numbers: Iterable[int]) -> int:
    """
    Return the maximum value from an iterable of integers.

    Args:
        numbers: Iterable containing integers

    Returns:
        The maximum integer

    Raises:
        ValueError: If the iterable is empty
    """
    numbers = list(numbers)

    if not numbers:
        raise ValueError("Cannot determine max of empty iterable")

    max_value = numbers[0]

    for number in numbers[1:]:
        if number > max_value:
            max_value = number

    return max_value


def is_palindrome(text: str) -> bool:
    """
    Check whether a string is a palindrome.

    Args:
        text: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    normalized = "".join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]


def sum_unique(numbers: Iterable[int]) -> int:
    """
    Sum only unique values from an iterable.

    Args:
        numbers: Iterable containing integers

    Returns:
        The sum of unique integers
    """
    return sum(set(numbers))


def calculate_fibonacci(limit: int) -> list[int]:
    """
    Generate a Fibonacci sequence up to a given limit.

    Args:
        limit: Number of elements to generate

    Returns:
        A list containing the Fibonacci sequence
    """
    if limit <= 0:
        return []

    sequence = [0, 1]

    while len(sequence) < limit:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[:limit]
