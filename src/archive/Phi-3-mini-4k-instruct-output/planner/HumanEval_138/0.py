def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
    Action Plan:
    1. Define a function `is_equal_to_sum_even` that takes an integer `n` as input.
    2. Initialize a variable to store the result (e.g., `is_possible`).
    3. Iterate from 2 to `n/4` (inclusive) with a step of 2 (to consider only even numbers).
    4. For each iteration, check if the current number is less than or equal to `n`.
    5. If the current number is less than or equal to `n`, subtract it from `n` and check if the remaining value is also less than or equal to `n`.
    6. If both conditions are met, set `is_possible` to `True` and break the loop.
    7. After the loop, return `is_possible` as the result.
    8. Test the function with example inputs to verify its correctness.
    """
    is_possible = False
    for i in range(2, n//4 + 1, 2):
        if i <= n and n - i <= n//4:
            is_possible = True
            break
    return is_possible