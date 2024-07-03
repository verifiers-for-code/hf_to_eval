from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    

    Action Plan:
    1. Initialize an empty list to store the filtered strings.
    2. Iterate through each string in the input list:
       a. Check if the string starts with the given prefix.
       b. If it does, add the string to the filtered list.
    3. Return the filtered list containing only the strings that start with the given prefix."""
    
    filtered_strings = []
    for string in strings:
        if string.startswith(prefix):
            filtered_strings.append(string)
    return filtered_strings