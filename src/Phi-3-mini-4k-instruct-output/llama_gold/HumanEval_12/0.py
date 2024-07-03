from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    

    Action Plan:
    1. Check if the input list is empty. If it is, return None.
    2. Find the maximum length of all strings in the input list.
    3. Iterate through the input list:
       a. For each string, check if its length is equal to the maximum length found.
       b. If it is, return this string (since it's the first longest string found).
    4. Note: The function will return as soon as it finds the first longest string, so it will return the first one in case of multiple strings with the same maximum length."""

    if not strings:
        return None

    max_length = max(len(s) for s in strings)

    for s in strings:
        if len(s) == max_length:
            return s