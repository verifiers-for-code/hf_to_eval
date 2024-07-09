def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    

    Action Plan:
    1. Define the function `is_equal_to_sum_even` with a single parameter `n`.
    2. Initialize a loop to generate all possible combinations of 4 positive even numbers.
    3. Within the loop, generate each combination using a nested loop structure:
        a. Iterate over possible even numbers (2, 4, 6, 8, 10, 12, 14, 16, 18, 20).
        b. Iterate over possible even numbers (2, 4, 6, 8, 10, 12, 14, 16, 18, 20).
        c. Iterate over possible even numbers (2, 4, 6, 8, 10, 12, 14, 16, 18, 20).
        d. Iterate over possible even numbers (2, 4, 6, 8, 10, 12, 14, 16, 18, 20).
    4. Calculate the sum of each combination.
    5. Check if the sum equals the given number `n`.
    6. If the sum equals `n`, return `True`.
    7. If no combination sums to `n`, return `False`.
    
    Note: Be careful with the loop structure and iteration ranges to generate all possible combinations.
    Consider using a more efficient approach, such as generating combinations using recursion or memoization, to reduce the number of iterations."""
    
    even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    for a in even_numbers:
        for b in even_numbers:
            for c in even_numbers:
                for d in even_numbers:
                    if a + b + c + d == n:
                        return True
    return False