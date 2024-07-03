from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    
    Parameters:
    strings (List[str]): A list of strings to concatenate
    
    Returns:
    str: A single concatenated string
    
    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
    Action Plan:
    1. Define the function `concatenate` with a single parameter `strings` of type `List[str]`:
       - This function will take a list of strings as input and return a single concatenated string
    
    2. Initialize an empty string to store the concatenated result:
       - This string will be used to build the final concatenated string
    
    3. Iterate through each string in the input list `strings`:
       - Use a loop or the `join()` method to concatenate each string to the result string
       - Use an appropriate separator (e.g., an empty string) to concatenate the strings
    
    4. Return the final concatenated string:
       - The function should return the concatenated string as the result
    
    Additional implementation details:
    - Consider using the `join()` method to concatenate the strings, as it's more efficient and concise than a loop
    - Ensure the function handles empty input lists correctly, returning an empty string in such cases
    - Consider adding input validation to check if the input is a list of strings, and raise an error if it's not
    """
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        raise ValueError("Input must be a list of strings")
    
    return ''.join(strings)