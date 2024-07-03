from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
    Action Plan:
    1. Understand the XOR operation: 
       - 1 XOR 1 = 0
       - 0 XOR 0 = 0
       - 1 XOR 0 = 1
       - 0 XOR 1 = 1
    2. Initialize an empty result string to store the XOR output.
    3. Iterate through both input strings simultaneously:
       - Use a method to pair corresponding characters from both strings.
    4. For each pair of characters:
       - Compare them using the XOR logic.
       - Append the result ('0' or '1') to the result string.
    5. After processing all characters, return the final result string.
    
    Note: Remember to handle strings of equal length only.
    """
    # Check if the input strings have the same length
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")

    # Initialize an empty result string
    result = ""

    # Iterate through both input strings simultaneously
    for char_a, char_b in zip(a, b):
        # Perform XOR operation on the corresponding characters
        xor_result = '1' if char_a != char_b else '0'
        # Append the result to the result string
        result += xor_result

    # Return the final result string
    return result