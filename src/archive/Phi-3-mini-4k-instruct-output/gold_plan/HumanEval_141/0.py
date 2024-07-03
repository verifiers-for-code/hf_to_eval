def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    """
    # Step 1: Define a list of valid file extensions
    valid_extensions = ['txt', 'exe', 'dll']

    # Step 2: Split the file_name string using '.' as the separator
    parts = file_name.split('.')

    # Step 3: Check if the split result has exactly 2 parts
    if len(parts) != 2:
        return 'No'

    # Step 4: Check if the extension (second part) is in the list of valid extensions
    if parts[1] not in valid_extensions:
        return 'No'

    # Step 5: Check if the name part (first part) is not empty
    if not parts[0]:
        return 'No'

    # Step 6: Check if the first character of the name part is a letter
    if not parts[0][0].isalpha():
        return 'No'

    # Step 7: Count the number of digits in the name part
    digit_count = sum(c.isdigit() for c in parts[0])

    # Step 8: If all checks pass, return 'Yes'
    if digit_count > 3:
        return 'No'

    return 'Yes'