def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    

    Action Plan:
    1. Understand that the input is a string and the expected output is an integer representing the string's length.
    2. Use a built-in function in Python that returns the number of characters in the input string.
    3. Return the result of this built-in function as the length of the input string.
    
    Note: Familiarize yourself with Python's built-in functions and their uses."""
    
    # Step 2: Use the built-in function len() to get the length of the string
    length = len(string)
    
    # Step 3: Return the length of the string
    return length