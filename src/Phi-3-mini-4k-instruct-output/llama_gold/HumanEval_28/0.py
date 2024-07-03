from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    

    Action Plan:
    1. Initialize an empty string to store the concatenated result.
    2. Iterate through each string in the input list:
       a. Add the current string to the end of the result string.
    3. After iterating through all strings, return the fully concatenated result string."""
    
    result = ""
    for string in strings:
        result += string
    return result