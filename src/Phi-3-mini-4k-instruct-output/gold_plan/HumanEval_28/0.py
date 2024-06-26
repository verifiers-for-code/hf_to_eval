from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Step 1: Initialize an empty result string
    result = ""

    # Step 2: Check if the input list is empty
    if not strings:
        return result

    # Step 3: Iterate through each string in the input list
    for string in strings:
        # Step 3a: Add each string to the result string
        result += string

    # Step 4: Return the final result string
    return result