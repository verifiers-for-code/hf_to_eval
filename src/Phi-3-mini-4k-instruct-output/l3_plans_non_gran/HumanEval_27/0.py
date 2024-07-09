def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    

    Action Plan:
    1. Understand the problem: The task is to flip the case of a given string, meaning lowercase characters should become uppercase and vice versa.
    2. Identify the operation: The string method `swapcase()` can be used to achieve this task.
    3. Use the `swapcase()` method: Apply the `swapcase()` method to the input string to flip its case.
    4. Return the modified string: Return the resulting string with the flipped case.
    
    Note: The `swapcase()` method is a built-in string method in Python that swaps the case of all characters in a string."""
    return string.swapcase()