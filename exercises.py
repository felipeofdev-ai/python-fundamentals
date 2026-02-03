"""
Basic Python exercises to practice fundamentals.
"""

# Exercise 1: Sum of two numbers
def sum_numbers(a, b):
    return a + b


# Exercise 2: Check if a number is even
def is_even(number):
    return number % 2 == 0


# Exercise 3: Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


# Exercise 4: Find the maximum number in a list
def find_max(numbers):
    return max(numbers)


# Exercise 5: Reverse a string
def reverse_string(text):
    return text[::-1]


if __name__ == "__main__":
    print(sum_numbers(3, 5))
    print(is_even(10))
    print(count_vowels("Python Fundamentals"))
    print(find_max([1, 5, 3, 9, 2]))
    print(reverse_string("Python"))
