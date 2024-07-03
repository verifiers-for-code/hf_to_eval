def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Parameters:
    n (int): The upper limit of the range to sum.
    
    Returns:
    int: The sum of numbers from 1 to n.
    
    Example:
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
    """
    # Step 2: Initialize a variable to store the sum, set to 0.
    total_sum = 0
    
    # Step 3: Use a loop to iterate from 1 to n (inclusive).
    for i in range(1, n + 1):
        # Step 4: In each iteration, add the current number to the sum.
        total_sum += i
    
    # Step 5: After the loop, return the final sum.
    return total_sum

# Using the formula for the sum of an arithmetic series to optimize the function
def sum_to_n_optimized(n: int) -> int:
    """
    sum_to_n_optimized is a function that sums numbers from 1 to n using the formula for the sum of an arithmetic series.
    
    Parameters:
    n (int): The upper limit of the range to sum.
    
    Returns:
    int: The sum of numbers from 1 to n.
    
    Example:
    >>> sum_to_n_optimized(30)
    465
    >>> sum_to_n_optimized(100)
    5050
    >>> sum_to_n_optimized(5)
    15
    >>> sum_to_n_optimized(10)
    55
    >>> sum_to_n_optimized(1)
    1
    """
    # Step 6: Consider using a more efficient approach, such as the formula for the sum of an arithmetic series.
    return n * (n + 1) // 2