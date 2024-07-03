from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    
    Action Plan:
    1. Define the function with two parameters:
       - `strings`: a list of strings to be filtered
       - `prefix`: a string to filter by
    
    2. Initialize an empty list to store the filtered strings
       - This list will hold the strings that start with the given prefix
    
    3. Iterate through each string in the input list:
       a. Check if the current string starts with the given prefix
          - Use the `startswith()` method to perform the check
       b. If the string starts with the prefix:
          - Add the string to the filtered list
    
    4. After iterating through all strings, return the filtered list
       - This list contains only the strings that start with the given prefix
    
    Additional implementation details:
    - Use a for loop to iterate through the input list of strings
    - Use the `startswith()` method to check if a string starts with the given prefix
    - Use the `append()` method to add strings to the filtered list
    - Ensure the function handles empty input lists and prefixes correctly
    - Consider adding type hints and a docstring to the function for clarity and documentation
    """
    filtered_strings = []
    for string in strings:
        if string.startswith(prefix):
            filtered_strings.append(string)
    return filtered_strings