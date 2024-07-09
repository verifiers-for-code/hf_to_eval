from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Action Plan:
    1. Initialize an empty list to store all prefixes of the input string.
    2. Iterate over the input string using two nested loops:
        a. The outer loop iterates over the starting index of the prefix (from 0 to the length of the string).
        b. The inner loop iterates over the ending index of the prefix (from the starting index + 1 to the length of the string).
    3. Within the inner loop, extract the substring from the starting index to the ending index and add it to the list of prefixes.
    4. After iterating over all possible prefixes, sort the list of prefixes in order from shortest to longest.
    5. Return the sorted list of prefixes.
    
    Note: Consider using Python's built-in string slicing feature to extract substrings and list comprehensions for efficient prefix generation.
    """
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return sorted(prefixes)