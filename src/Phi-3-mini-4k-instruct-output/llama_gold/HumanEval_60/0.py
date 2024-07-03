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
    1. Initialize a variable to store the sum.
    2. Generate a sequence of numbers from 1 to n (inclusive).
    3. Iterate through this sequence and add each number to the sum variable.
    4. After iterating through all numbers, return the calculated sum."""
    
    # Step 1: Initialize a variable to store the sum
    total_sum = 0
    
    # Step 2: Generate a sequence of numbers from 1 to n (inclusive)
    for i in range(1, n+1):
        
        # Step 3: Iterate through this sequence and add each number to the sum variable
        total_sum += i
    
    # Step 4: After iterating through all numbers, return the calculated sum
    return total_sum