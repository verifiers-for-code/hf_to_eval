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
    1. Define a list of valid file extensions: ['txt', 'exe', 'dll']
    2. Split the file_name string using '.' as the separator
    3. Check if the split result has exactly 2 parts (name and extension)
       - If not, return 'No'
    4. Check if the extension (second part) is in the list of valid extensions
       - If not, return 'No'
    5. Check if the name part (first part) is not empty
       - If empty, return 'No'
    6. Check if the first character of the name part is a letter
       - If not, return 'No'
    7. Count the number of digits in the name part
       - If the count is greater than 3, return 'No'
    8. If all checks pass, return 'Yes'
    """
    valid_extensions = ['txt', 'exe', 'dll']
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    name, extension = parts
    if extension not in valid_extensions:
        return 'No'
    if not name:
        return 'No'
    if not name[0].isalpha():
        return 'No'
    digit_count = sum(c.isdigit() for c in name)
    if digit_count > 3:
        return 'No'
    return 'Yes'