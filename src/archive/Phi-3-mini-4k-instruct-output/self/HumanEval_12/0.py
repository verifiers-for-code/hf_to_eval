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
    1. Handle the case of an empty input list:
        - Return None if the input list is empty
    
    2. Use a variable to keep track of the longest string and its length:
        - Initialize this variable with the first string and its length
    
    3. Iterate through the list (excluding the first element):
        - Compare the length of the current string with the longest string
        - Update the longest string and length if a longer string is found
    
    4. Return the longest string found
    """
    if not strings:
        return None

    longest_str = strings[0]
    longest_len = len(longest_str)

    for string in strings[1:]:
        if len(string) > longest_len:
            longest_str = string
            longest_len = len(string)

    return longest_str