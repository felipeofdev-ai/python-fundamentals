"""
Module: data_types
Author: Felipe Fernandes

Examples of Python built-in data types and collections,
focused on practical usage and clean data manipulation.
"""

from typing import Iterable


def unique_items(items: Iterable[str]) -> set[str]:
    """
    Return a set of unique items from an iterable.

    Args:
        items: Iterable containing string values

    Returns:
        A set with unique values
    """
    return set(items)


def count_occurrences(items: Iterable[str]) -> dict[str, int]:
    """
    Count occurrences of each item in an iterable.

    Args:
        items: Iterable containing string values

    Returns:
        A dictionary mapping each item to its frequency
    """
    counts: dict[str, int] = {}

    for item in items:
        counts[item] = counts.get(item, 0) + 1

    return counts


def filter_positive_numbers(numbers: Iterable[int]) -> list[int]:
    """
    Filter only positive numbers from an iterable.

    Args:
        numbers: Iterable of integers

    Returns:
        A list containing only positive integers
    """
    return [n for n in numbers if n > 0]


def merge_dictionaries(
    base: dict[str, int], updates: dict[str, int]
) -> dict[str, int]:
    """
    Merge two dictionaries, summing values for common keys.

    Args:
        base: Base dictionary
        updates: Dictionary with values to merge

    Returns:
        A merged dictionary
    """
    result = base.copy()

    for key, value in updates.items():
        result[key] = result.get(key, 0) + value

    return result
