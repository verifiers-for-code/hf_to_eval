from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Step 1: Initialize an empty result string to store the concatenated output.
    result = ""

    # Step 2: Check if the input list is empty. If so, return the empty result string.
    if not strings:
        return result

    # Step 3: Iterate through each string in the input list:
    # a. Add each string to the result string.
    for string in strings:
        result += string

    # Step 4: After the iteration, return the final result string.
    return result