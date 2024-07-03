from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Initialize the concatenation result as an empty string
    result = ''
    
    # Use a loop to iterate through each string in the input list
    for string in strings:
        # Within the loop, add each string to the concatenation result
        result += string
    
    # Handle edge cases:
    # a. Empty input list
    if not strings:
        return ''
    # b. List with one or no strings
    elif len(strings) <= 1:
        return strings[0]
    
    # Return the concatenated result
    return result