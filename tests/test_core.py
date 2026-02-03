import pytest

from core.data_types import (
    unique_items,
    count_occurrences,
    filter_positive_numbers,
)
from core.oop import BankAccount
from exercises.mini_challenges import (
    find_max,
    is_palindrome,
    sum_unique,
    calculate_fibonacci,
)


def test_unique_items_removes_duplicates():
    items = ["a", "b", "a", "c"]
    result = unique_items(items)
    assert result == {"a", "b", "c"}


def test_count_occurrences_counts_correctly():
    items = ["apple", "banana", "apple"]
    result = count_occurrences(items)
    assert result == {"apple": 2, "banana": 1}


def test_filter_positive_numbers():
    numbers = [-2, 0, 3, 5, -1]
    result = filter_positive_numbers(numbers)
    assert result == [3, 5]


def test_bank_account_deposit_and_withdraw():
    account = BankAccount("Felipe", 100.0)

    account.deposit(50.0)
    assert account.balance == 150.0

    success = account.withdraw(40.0)
    assert success is True
    assert account.balance == 110.0


def test_bank_account_withdraw_insufficient_balance():
    account = BankAccount("Felipe", 20.0)
    success = account.withdraw(50.0)
    assert success is False
    assert account.balance == 20.0


def test_find_max_returns_max_value():
    numbers = [1, 7, 3, 9, 2]
    assert find_max(numbers) == 9


def test_find_max_raises_error_on_empty_iterable():
    with pytest.raises(ValueError):
        find_max([])


def test_is_palindrome_ignores_case_and_symbols():
    text = "A man, a plan, a canal: Panama"
    assert is_palindrome(text) is True


def test_sum_unique_sums_only_unique_values():
    numbers = [1, 2, 2, 3, 3, 3]
    assert sum_unique(numbers) == 6


def test_calculate_fibonacci_generates_sequence():
    result = calculate_fibonacci(5)
    assert result == [0, 1, 1, 2, 3]
