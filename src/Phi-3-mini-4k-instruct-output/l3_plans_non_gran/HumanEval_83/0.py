def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
    Action Plan:
    1. Define the function `starts_one_ends` with a parameter `n` representing the number of digits.
    2. Calculate the total number of n-digit positive integers using the formula `9 * 10 ** (n - 1)`.
    3. Count the numbers that start with 1:
        - Calculate the count of numbers that start with 1 and end with 0, which is `10 ** (n - 1)`.
        - Calculate the count of numbers that start with 1 and end with 1, which is `10 ** (n - 2)`.
        - Add these two counts together to get the total count of numbers that start with 1.
    4. Count the numbers that end with 1:
        - Calculate the count of numbers that start with 0 and end with 1, which is `10 ** (n - 1)`.
        - Calculate the count of numbers that start with 1 and end with 1, which is `10 ** (n - 2)`.
        - Add these two counts together to get the total count of numbers that end with 1.
    5. Return the sum of the counts of numbers that start with 1 and end with 1."""
    
    total_count = 9 * 10 ** (n - 1)
    start_with_one_count = 10 ** (n - 1) + 10 ** (n - 2)
    end_with_one_count = 10 ** (n - 1) + 10 ** (n - 2)
    
    return start_with_one_count + end_with_one_count