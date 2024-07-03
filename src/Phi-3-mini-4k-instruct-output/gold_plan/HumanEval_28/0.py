from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'

    Action Plan:
    1. Initialize an empty result string to store the concatenated output.
    2. Check if the input list is empty. If so, return the empty result string.
    3. Iterate through each string in the input list:
       a. Add each string to the result string.
    4. After the iteration, return the final result string.

    Hint: Consider using a built-in Python function that can efficiently
    join multiple strings together instead of manual concatenation.
    """
    result = ''
    if not strings:
        return result
    for string in strings:
        result += string
    return result