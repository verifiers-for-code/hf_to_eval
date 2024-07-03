def strlen(string: str) -> int:
    """
    Return the length of a given string.
    
    This function calculates the length of a given string using the built-in `len()` function.
    
    Args:
        string (str): The input string.
        
    Returns:
        int: The length of the input string.
        
    Raises:
        TypeError: If the input is not a string.
        
    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    # Input validation
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")
    
    # Calculate the string's length
    length = len(string)
    
    # Return the length
    return length