from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    
    Action Plan:
    1. Check if the input list is empty:
        - If empty, return None immediately
    2. Initialize two variables:
        - longest_string: to store the longest string found so far
        - longest_length: to store the length of the longest string
    3. Iterate through each string in the input list:
        - For each string, calculate its length
        - Compare the length of the current string with the longest_length
        - If the current string is longer:
            - Update longest_string with the current string
            - Update longest_length with the current string's length
    4. After iterating through all strings, return the longest_string
    Note: Use appropriate string methods for length calculation and comparison.
    Be careful to handle the edge case of an empty input list correctly.
    """
    if not strings:
        return None

    longest_string = strings[0]
    longest_length = len(longest_string)

    for string in strings[1:]:
        if len(string) > longest_length:
            longest_string = string
            longest_length = len(string)

    return longest_string

# Test cases
print(longest([]))  # Should return None
print(longest(['a', 'b', 'c']))  # Should return 'a'
print(longest(['a', 'bb', 'ccc']))  # Should return 'ccc'