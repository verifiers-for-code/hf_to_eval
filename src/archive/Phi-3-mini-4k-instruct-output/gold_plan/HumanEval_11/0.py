from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Step 2: Initialize an empty result string to store the XOR output.
    result = ''

    # Step 3: Iterate through both input strings simultaneously.
    for char_a, char_b in zip(a, b):
        # Step 4: For each pair of characters, compare them using the XOR logic.
        if char_a == char_b:
            result += '0'
        else:
            result += '1'

    # Step 5: After processing all characters, return the final result string.
    return result