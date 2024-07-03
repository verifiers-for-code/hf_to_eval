from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
    Action Plan:
    1. Define the function with two string parameters, a and b, representing binary strings.
    2. Convert the input strings a and b to binary format using the int function with base 2.
    3. Perform binary XOR operation on the two binary numbers using the ^ operator.
    4. Convert the result back to a binary string using the bin function and remove the '0b' prefix.
    5. Return the resulting binary string.
    6. Consider adding error handling for cases where the input strings are not valid binary strings (i.e., contain characters other than '0' and '1').
    """
    # Check if the input strings are valid binary strings
    if not all(char in '01' for char in a) or not all(char in '01' for char in b):
        raise ValueError("Input strings must consist only of 1s and 0s.")
    
    # Convert the input strings to binary format
    a_bin = int(a, 2)
    b_bin = int(b, 2)
    
    # Perform binary XOR operation
    result_bin = a_bin ^ b_bin
    
    # Convert the result back to a binary string and remove the '0b' prefix
    result_str = bin(result_bin)[2:]
    
    return result_str