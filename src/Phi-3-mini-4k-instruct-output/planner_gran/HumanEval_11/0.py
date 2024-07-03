from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    1. Define the function signature:
       - Name: string_xor
       - Parameters: a (str), b (str)
       - Return type: str
    
    2. Initialize an empty list to store the XOR result:
       - This list will hold the characters of the XOR result as strings
    
    3. Iterate over the characters of the input strings:
       a. For each character in string a:
          - Compare the character with the corresponding character in string b
          - Perform the XOR operation (using the ^ operator)
          - Convert the result to a string and append it to the result list
       b. Repeat step a for each character in string b
    
    4. Join the characters in the result list into a single string:
       - Use the join() method to concatenate the characters
    
    5. Return the XOR result string:
       - Ensure the result is a string of 0s and 1s
    
    Additional implementation details:
    - Use a loop or list comprehension to iterate over the characters of the input strings
    - Use the ^ operator for the XOR operation
    - Convert the result of the XOR operation to a string using the str() function
    - Handle edge cases, such as empty input strings or strings of different lengths
    - Consider adding type hints and a docstring to the function for clarity and documentation
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")
    
    result = [str(int(a[i]) ^ int(b[i])) for i in range(len(a))]
    return ''.join(result)