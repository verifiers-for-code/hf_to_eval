from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    
    Args:
    string (str): The input string from which prefixes are to be generated.
    
    Returns:
    List[str]: A list of all prefixes from shortest to longest.
    
    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = [string[:i+1] for i in range(len(string))]
    return prefixes