from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    
    Action Plan:
    1. Begin by defining the filter_by_substring function with the appropriate parameters
    2. Implement list comprehension within the function to iterate over each string in the list:
        a. Use the `in` keyword to check if the substring is present in the current string
    
    3. Create a condition in the list comprehension to determine inclusion based on the presence of the substring
    
    4. Construct and return the resulting filtered list of strings, ensuring to check that no strings contain the given substring
    
    5. Provide test cases, including:
        a. An empty input list
        b. A list containing various strings to check different substring scenarios
    
    6. Optimize the code for readability and performance, making use of Python's concise syntax
    """
    return [string for string in strings if substring in string]