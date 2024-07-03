from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
    Action Plan:
    1. Start with a helper function for XOR operation on two digits
    2. Use a loop or list comprehension to iterate over the length of the shorter string, comparing corresponding digits from both strings
    3. For each pair of digits, call the helper function and accumulate the result
    4. Handle differences in string lengths with appropriate comparison logic (padding with '0')
    5. Return the accumulated result as a string
    6. Test the function with given examples and edge cases, such as strings of uneven lengths or strings with a different number of characters
    """
    
    def xor_digits(digit_a: str, digit_b: str) -> str:
        """Helper function to perform XOR operation on two digits."""
        return '1' if digit_a != digit_b else '0'
    
    # Determine the length of the shorter string
    min_length = min(len(a), len(b))
    
    # Perform XOR operation on corresponding digits and accumulate the result
    result = ''.join(xor_digits(a[i], b[i]) for i in range(min_length))
    
    # Pad the result with '0's if one string is longer than the other
    if len(a) > len(b):
        result += '0' * (len(a) - len(b))
    elif len(b) > len(a):
        result += '0' * (len(b) - len(a))
    
    return result