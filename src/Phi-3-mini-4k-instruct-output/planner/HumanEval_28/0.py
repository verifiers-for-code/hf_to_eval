from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    
    Parameters:
    strings (List[str]): A list of strings to be concatenated.
    
    Returns:
    str: A single string that is the concatenation of all the strings in the input list.
    
    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Check if the input list is empty
    if not strings:
        return ''
    
    # Use the join method to concatenate the strings in the list
    return ''.join(strings)