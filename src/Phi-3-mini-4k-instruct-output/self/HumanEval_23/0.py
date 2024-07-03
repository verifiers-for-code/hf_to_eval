def strlen(string: str) -> int:
    """
    Return length of given string
    
    Input:
    - string (str): A string to calculate the length of
    
    Output:
    - int: The length of the input string
    
    This function calculates the length of a given string using the built-in `len()` function.
    It returns the length of the string if it's a valid string input.
    If the input is not a string, it returns -1.
    """
    
    # Input validation
    if not isinstance(string, str):
        return -1
    
    # Calculate the string's length
    length = len(string)
    
    # Return the length
    return length