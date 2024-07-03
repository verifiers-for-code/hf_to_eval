from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
    1. Initialize an empty list to store the filtered strings
       - This list will hold the strings that contain the given substring
    
    2. Iterate through each string in the input list of strings:
       - Use a loop to process each string individually
    
    3. Check if the given substring is present in the current string:
       - Use the 'in' operator or a string method to perform the substring check
    
    4. If the substring is found in the string:
       - Add the string to the filtered list
       - Use a list method to append the string to the filtered list
    
    5. After iterating through all strings, return the filtered list:
       - The list now contains only the strings that contain the given substring
    
    Additional implementation details:
    - Use a loop (e.g., for loop) to iterate through the input list of strings
    - Use a conditional statement (e.g., if statement) to check if the substring is present in each string
    - Use a list method (e.g., append) to add strings to the filtered list
    - Ensure the function handles empty input lists and substrings correctly
    - Consider using a list comprehension as an alternative to the loop and conditional statement
    """
    filtered_strings = []
    for string in strings:
        if substring in string:
            filtered_strings.append(string)
    return filtered_strings