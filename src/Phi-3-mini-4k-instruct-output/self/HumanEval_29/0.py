from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    

    Action Plan:
    1. Define the main function and parameters
    
    2. Handle empty input list:
        - Return an empty list if the input list is empty
    
    3. Implement list filtering logic:
        a. Iterate through each string in the input list
        b. Use string slicing or a built-in function to check if the string starts with the given prefix
    
    4. Populate the new list with filtered strings
    
    5. Return the new list
    
    6. Optimization considerations:
        - Evaluate using slicing for string prefix comparison vs. using `str.startswith()`
    
    7. Test cases verification:
        - Ensure the function works correctly for all specified test cases and common scenarios
    """
    if not strings:
        return []

    filtered_strings = [string for string in strings if string.startswith(prefix)]
    return filtered_strings