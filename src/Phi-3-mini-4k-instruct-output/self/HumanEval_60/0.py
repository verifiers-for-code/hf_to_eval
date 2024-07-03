def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    

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
    
    5. Verify the function's accuracy against the provided test cases and consider additional edge cases, such as zero and negative input values"""

    # Check for edge cases
    if n < 1:
        return 0

    # Calculate the sum using the formula
    return int(n * (n + 1) / 2)