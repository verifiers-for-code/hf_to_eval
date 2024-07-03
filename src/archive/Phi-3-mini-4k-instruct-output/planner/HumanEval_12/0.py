from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    >>> longest([])
    None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'

    Action Plan:
    1. Check if the input list is empty:
        - If true, return None immediately
    2. Initialize two variables:
        - longest_string: to store the longest string found so far
        - longest_length: to store the length of the longest string found so far
    3. Iterate through each string in the input list:
        - For each string, calculate its length
        - Compare the length with the current longest_length:
            - If the current string's length is greater, update longest_string and longest_length
    4. After iterating through all strings, return longest_string
    5. If the input list is empty, return None

    Note: Use the built-in len() function to calculate the length of each string.
    Be careful to update the longest_string and longest_length variables correctly."""
    
    if not strings:
        return None
    
    longest_string = strings[0]
    longest_length = len(longest_string)
    
    for string in strings:
        string_length = len(string)
        if string_length > longest_length:
            longest_string = string
            longest_length = string_length
    
    return longest_string