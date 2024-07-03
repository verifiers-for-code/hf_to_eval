def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    
    Action Plan:
    1. Understand the input: 'n' is the upper limit of the range to sum.
    2. Create a sequence of numbers from 1 to n (inclusive).
    3. Sum all the numbers in this sequence.
    4. Return the total sum.

    Implementation steps:
    1. Consider how to generate a sequence of numbers from 1 to n.
       Hint: Python has a built-in function to create ranges of numbers.
    2. Find a way to sum all numbers in the sequence efficiently.
       Hint: There's a built-in function in Python that can sum iterables.
    3. Combine the generation of the sequence and the summing operation.
    4. Return the result of the sum operation.

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
    # Generate a sequence of numbers from 1 to n (inclusive)
    sequence = range(1, n + 1)
    
    # Sum all the numbers in the sequence
    total_sum = sum(sequence)
    
    # Return the result of the sum operation
    return total_sum