from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
    Action Plan:
    1. Initialize an empty list to store the filtered strings.
    2. Iterate through each string in the input 'strings' list.
    3. For each string, check if it starts with the given 'prefix'.
    4. If the string starts with the prefix, add it to the filtered list.
    5. After checking all strings, return the filtered list.
    
    Hint: Consider using a list comprehension to make the code more concise.
    Remember to use the 'startswith()' method to check if a string begins with the prefix.
    """
    return [string for string in strings if string.startswith(prefix)]