from typing import List

def xor_digits(a: str, b: str) -> str:
    """ Helper function to perform XOR operation on two digits """
    return '1' if a != b else '0'

def string_xor(a: str, b: str) -> str:
    """ Perform binary XOR on two strings consisting only of 1s and 0s """
    # Step 2: Use a loop to iterate over the length of the shorter string
    result = ''
    for i in range(min(len(a), len(b))):
        # Step 3: Call the helper function and accumulate the result
        result += xor_digits(a[i], b[i])
    
    # Step 4: Handle differences in string lengths
    if len(a) > len(b):
        result += a[len(b):]
    elif len(b) > len(a):
        result += b[len(a):]
    
    # Step 5: Return the accumulated result as a string
    return result