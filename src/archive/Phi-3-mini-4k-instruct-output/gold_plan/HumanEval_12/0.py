from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])
    None
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    # Step 1: Check if the input list is empty
    if not strings:
        return None

    # Step 2: Find the maximum length among all strings
    max_length = max(len(s) for s in strings)

    # Step 3: Iterate through the list of strings
    for string in strings:
        if len(string) == max_length:
            return string

    # Step 4: (Not necessary, but included for completeness)
    # If no string is returned after the loop, return None
    return None