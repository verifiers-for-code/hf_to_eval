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
    

    Action Plan:
    1. Split the file_name at the dot character using split() and store the parts in variables:
        - prefix (before the dot)
        - suffix (after the dot)
    
    2. Validate the prefix part:
        a. Check length for digits using isdigit()
        b. Ensure prefix is non-empty and starts with a Latin alphabet character
        c. Return 'No' if any condition is not met
    
    3. Validate the suffix part:
        a. Check if suffix is 'txt', 'exe', or 'dll'
        b. Return 'No' if the suffix is not one of the valid options
    
    4. If both parts pass their checks, return 'Yes'
    5. Special considerations:
        a. Uppercase and lowercase letters are equal; use string methods for case-insensitive comparisons
        b. Properly handle edge cases such as file names without a dot"""

    # Step 1: Split the file_name at the dot character
    parts = file_name.split('.')

    # Check if there is exactly one dot
    if len(parts) != 2:
        return 'No'

    # Step 2: Validate the prefix part
    prefix = parts[0]
    if len(prefix) == 0 or prefix.isdigit() or not prefix[0].isalpha():
        return 'No'

    # Step 3: Validate the suffix part
    suffix = parts[1]
    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    # If both parts pass their checks, return 'Yes'
    return 'Yes'