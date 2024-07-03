from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor_digits(digit_a: str, digit_b: str) -> str:
        """Helper function to perform XOR operation on two digits."""
        return '1' if digit_a != digit_b else '0'

    # Determine the length of the shorter string
    min_length = min(len(a), len(b))

    # Perform XOR operation on corresponding digits
    result = ''.join(xor_digits(a[i], b[i]) for i in range(min_length))

    # Pad the result with '0's if one string is longer than the other
    if len(a) > min_length:
        result += '0' * (len(a) - min_length)
    elif len(b) > min_length:
        result += '0' * (len(b) - min_length)

    return result