import re

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Initialize a counter for digits in the file name
    digit_count = sum(c.isdigit() for c in file_name)
    
    # Check for the presence of a dot in the file name
    if file_name.count('.') > 1:
        return 'No'
    
    # Validate the first substring (before the dot)
    parts = file_name.split('.')
    if len(parts) != 2 or not parts[0] or not parts[0][0].isalpha():
        return 'No'
    
    # Validate the second substring (after the dot)
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # If all conditions are met, return 'Yes'
    return 'Yes'