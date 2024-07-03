def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    

    Action Plan:
    1. Define a function `flip_case` that takes a string as input.
    2. Identify the built-in string method for case conversion: `swapcase()`.
    3. Apply the `swapcase()` method to the input string to flip the case of each character.
    4. Return the resulting string with the case flipped.
    
    Note: The `swapcase()` method is a built-in string method in Python that flips the case of each character in the string."""
    return string.swapcase()