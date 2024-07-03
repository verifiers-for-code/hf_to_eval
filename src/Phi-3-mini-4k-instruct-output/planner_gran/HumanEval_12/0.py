from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    >>> longest([])
    
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
    1. Handle the input list and edge cases:
       - Check if the input list is empty
       - If empty, return None immediately
    
    2. Initialize variables to keep track of the longest string:
       - Set the longest string to an empty string (or a default value)
    
    3. Iterate through each string in the input list:
       - Compare the length of the current string with the length of the longest string found so far
       - If the current string is longer, update the longest string
    
    4. After iterating through all strings, return the longest string found
    
    Additional implementation details:
    - Use a for loop to iterate through the input list
    - Use the len() function to compare the lengths of strings
    - Use a conditional statement (if) to update the longest string when a longer string is found
    - Ensure that the function handles empty input lists correctly
    - Consider using a more descriptive variable name instead of 'longest_string'"""
    
    if not strings:
        return None
    
    longest_string = strings[0]
    
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    
    return longest_string