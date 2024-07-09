from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
    Action Plan:
    1. Validate inputs:
        - Check if both inputs (a and b) are strings
        - Ensure both strings consist only of '0' and '1' characters
        - Raise a ValueError if either input is invalid
    
    2. Convert the input strings to lists of integers:
        - Use a list comprehension to iterate over each character in the strings
        - Convert each character to an integer (0 or 1) using the int() function
    
    3. Perform the XOR operation:
        - Use the zip() function to iterate over the corresponding elements of the two lists
        - Apply the XOR operation (^) to each pair of elements
        - Store the results in a new list
    
    4. Convert the result back to a string:
        - Use the join() method to concatenate the elements of the result list into a single string
        - Use a string joiner ('') to separate the elements
    
    5. Return the final result:
        - Return the resulting string as the output of the function
    """
    # Validate inputs
    if not isinstance(a, str) or not isinstance(b, str):
        raise ValueError("Both inputs must be strings")
    if not all(c in '01' for c in a) or not all(c in '01' for c in b):
        raise ValueError("Both strings must consist only of '0' and '1' characters")
    
    # Convert input strings to lists of integers
    a_int = [int(c) for c in a]
    b_int = [int(c) for c in b]
    
    # Perform XOR operation
    xor_result = [x ^ y for x, y in zip(a_int, b_int)]
    
    # Convert result back to string
    result_str = ''.join(str(c) for c in xor_result)
    
    return result_str