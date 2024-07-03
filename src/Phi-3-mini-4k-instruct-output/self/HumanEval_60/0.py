def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Action Plan:
    1. Discuss the concept of the sum of arithmetic series:
        a. This series has a known formula: n * (n + 1) / 2
    2. Explain how to implement the formula:
        a. Use the input number `n` as the upper limit in the formula
        b. Handle integer and fractional `n` values, accounting for the difference between the formula's result and the exact sum of the series
    3. Address edge cases:
        a. For small positive integers (e.g., 1 to n), where the direct calculation will yield the exact result
        b. For large numbers, it might be helpful to compare the direct formula's result with the result of calculating the sum through iteration
    4. Optimize:
        - Since this is a problem with a direct formula, iteration is not necessary, ensuring optimal performance
    
    5. Verify the function's accuracy against the provided test cases and consider additional edge cases, such as zero and negative input values
    """
    if n < 0:
        return "Error: Input must be a non-negative integer."
    elif n == 0:
        return 0
    else:
        return int(n * (n + 1) / 2)