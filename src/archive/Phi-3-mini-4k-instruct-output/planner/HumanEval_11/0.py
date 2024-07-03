from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): A binary string consisting only of 1s and 0s.
    b (str): A binary string consisting only of 1s and 0s.

    Returns:
    str: The result of binary XOR operation on a and b, represented as a binary string.

    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Step 2: Convert the input strings a and b to binary format using the int function with base 2.
    a_bin = int(a, 2)
    b_bin = int(b, 2)

    # Step 3: Perform binary XOR operation on the two binary numbers using the ^ operator.
    xor_result = a_bin ^ b_bin

    # Step 4: Convert the result back to a binary string using the bin function and remove the '0b' prefix.
    result_bin = bin(xor_result)[2:]

    # Step 5: Return the resulting binary string.
    return result_bin

# Step 6: Add error handling for cases where the input strings are not valid binary strings (i.e., contain characters other than '0' and '1').
def string_xor_with_error_handling(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Args:
    a (str): A binary string consisting only of 1s and 0s.
    b (str): A binary string consisting only of 1s and 0s.

    Returns:
    str: The result of binary XOR operation on a and b, represented as a binary string.

    Raises:
    ValueError: If either a or b contains characters other than '0' and '1'.

    Example:
    >>> string_xor_with_error_handling('010', '110')
    '100'
    """
    # Check if the input strings are valid binary strings
    if not all(char in '01' for char in a) or not all(char in '01' for char in b):
        raise ValueError("Input strings must consist only of 1s and 0s.")

    # Perform the XOR operation
    return string_xor(a, b)