from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    

    Action Plan:
    1. Confirm that the input strings a and b only contain '1's and '0's.
    2. Define a helper function to perform binary XOR on two characters (i and j):
       a. If i and j are the same, return '0'.
       b. If i and j are different, return '1'.
    3. Initialize an empty result string to store the XOR result.
    4. Iterate through the characters of a and b in parallel (using a method to iterate through both strings simultaneously):
       a. For each pair of characters, apply the XOR helper function.
       b. Append the result to the result string.
    5. Return the complete result string after processing all characters."""

    # Helper function to perform binary XOR on two characters
    def xor_char(i: str, j: str) -> str:
        if i == j:
            return '0'
        else:
            return '1'

    # Check if input strings only contain '1's and '0's
    if not (set(a).issubset({'0', '1'}) and set(b).issubset({'0', '1'})):
        raise ValueError("Input strings must only contain '1's and '0's")

    # Initialize an empty result string
    result = ''

    # Iterate through the characters of a and b in parallel
    for i, j in zip(a, b):
        # Apply the XOR helper function and append the result
        result += xor_char(i, j)

    # Return the complete result string
    return result