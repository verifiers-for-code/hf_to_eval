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
    1. Check if the input list is empty. If so, return None immediately.
    2. If the list is not empty, find the maximum length among all strings:
       a. Use a list comprehension to get the length of each string.
       b. Use the max() function to find the maximum length.
    3. Iterate through the list of strings:
       a. For each string, check if its length equals the maximum length found.
       b. If a match is found, return that string immediately (this ensures we return the first occurrence).
    4. (Note: Step 4 is not necessary as we will always return in step 3, but including for completeness)
       If no string is returned after the loop, return None (this case should never occur if steps 1-3 are implemented correctly).

    Remember to use type hinting for the function parameters and return value as shown in the function definition.
    """
    if not strings:
        return None

    max_length = max(len(s) for s in strings)

    for s in strings:
        if len(s) == max_length:
            return s

    return None