def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    
    Parameters:
    n (int): A non-negative integer representing the upper limit of the sequence.
    
    Returns:
    str: A string containing space-delimited numbers from 0 to n inclusive.
    
    Raises:
    ValueError: If n is negative or not an integer.
    
    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    
    # Validate the input parameter n
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Generate the sequence of numbers
    sequence = [str(i) for i in range(n+1)]
    
    # Join the strings with spaces
    result = " ".join(sequence)
    
    # Return the final string
    return result