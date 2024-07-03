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
    1. Split the input file_name into two parts using the dot '.' as a separator.
    2. Check if the resulting list has exactly two elements. If not, return 'No'.
    3. Verify that the second part (suffix) is one of the allowed values ('txt', 'exe', 'dll'). If not, return 'No'.
    4. Check that the first part (prefix) is not empty. If it is, return 'No'.
    5. Verify that the first character of the prefix is a letter (either lowercase or uppercase). If not, return 'No'.
    6. Count the number of digits in the prefix. If there are more than 3, return 'No'.
    7. If all conditions are met, return 'Yes'. Otherwise, return 'No'."""

    # Step 1: Split the input file_name into two parts using the dot '.' as a separator.
    parts = file_name.split('.')

    # Step 2: Check if the resulting list has exactly two elements. If not, return 'No'.
    if len(parts) != 2:
        return 'No'

    # Step 3: Verify that the second part (suffix) is one of the allowed values ('txt', 'exe', 'dll'). If not, return 'No'.
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    # Step 4: Check that the first part (prefix) is not empty. If it is, return 'No'.
    if not parts[0]:
        return 'No'

    # Step 5: Verify that the first character of the prefix is a letter (either lowercase or uppercase). If not, return 'No'.
    if not parts[0][0].isalpha():
        return 'No'

    # Step 6: Count the number of digits in the prefix. If there are more than 3, return 'No'.
    digit_count = sum(c.isdigit() for c in parts[0])
    if digit_count > 3:
        return 'No'

    # Step 7: If all conditions are met, return 'Yes'. Otherwise, return 'No'.
    return 'Yes'