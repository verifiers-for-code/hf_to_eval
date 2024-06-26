def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the range to sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Action Plan:
    1. Understand the input: 'n' is the upper limit of the range to sum.
    2. Create a sequence of numbers from 1 to n (inclusive).
    3. Sum all the numbers in this sequence.
    4. Return the total sum.

    Implementation steps:
    1. Generate a sequence of numbers from 1 to n using the built-in `range` function.
    2. Use the built-in `sum` function to sum all numbers in the sequence.
    3. Return the result of the sum operation.
    """
    # Generate a sequence of numbers from 1 to n (inclusive)
    sequence = range(1, n + 1)
    
    # Sum all numbers in the sequence
    total_sum = sum(sequence)
    
    return total_sum