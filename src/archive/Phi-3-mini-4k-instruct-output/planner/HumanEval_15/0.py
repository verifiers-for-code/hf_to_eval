def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
    n (int): The upper limit of the sequence (inclusive).

    Returns:
    str: A string containing space-delimited numbers from 0 to n (inclusive).

    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Step 1: Generate the sequence of numbers
    numbers = [str(i) for i in range(n+1)]
    
    # Step 4: Join the numbers with spaces
    result = ' '.join(numbers)
    
    # Step 5: Return the final result
    return result