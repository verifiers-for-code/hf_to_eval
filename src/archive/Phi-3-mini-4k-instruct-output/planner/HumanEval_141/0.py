def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.

    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphabets ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']

    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphabets letter)

    Action Plan:
    1. Define the function `file_name_check` with a single parameter `file_name`.
    2. Check if the file name is a string and has at least one character. If not, return 'No'.
    3. Count the number of digits in the file name using a loop or a string method.
    4. Check if the file name contains exactly one dot '.' using the `count` method.
    5. Split the file name into two parts using the dot as a separator.
    6. Validate the substring before the dot:
        a. Check if it's not empty.
        b. Check if it starts with a letter from the latin alphabets ('a'-'z' or 'A'-'Z').
    7. Validate the substring after the dot:
        a. Check if it's one of the allowed substrings ('txt', 'exe', 'dll').
    8. If all conditions are met, return 'Yes'. Otherwise, return 'No'."""

    if not isinstance(file_name, str) or len(file_name) == 0:
        return 'No'

    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    if not parts[0] or not parts[0][0].isalpha():
        return 'No'

    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'