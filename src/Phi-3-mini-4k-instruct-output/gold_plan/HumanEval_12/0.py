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
    """
    # Step 1: Check if the input list is empty
    if not strings:
        return None

    # Step 2: Find the maximum length among all strings
    max_length = max(len(s) for s in strings)

    # Step 3: Iterate through the list of strings and return the first one with the maximum length
    for s in strings:
        if len(s) == max_length:
            return s

    # Step 4: This step is not necessary as we will always return in step 3, but included for completeness
    return None