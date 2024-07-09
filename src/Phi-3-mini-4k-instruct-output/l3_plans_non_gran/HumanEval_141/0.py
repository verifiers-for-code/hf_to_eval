def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphabet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    # Initialize a variable to store the result (initially set to 'No')
    result = 'No'
    
    # Check if the file name contains more than three digits
    if file_name.count('0') + file_name.count('1') + file_name.count('2') + \
       file_name.count('3') + file_name.count('4') + file_name.count('5') + \
       file_name.count('6') + file_name.count('7') + file_name.count('8') + \
       file_name.count('9') > 3:
        return result
    
    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return result
    
    # Check the substring before the dot
    dot_index = file_name.find('.')
    if dot_index == -1 or dot_index == 0 or not file_name[dot_index-1].isalpha():
        return result
    
    # Check the substring after the dot
    extension = file_name[dot_index+1:]
    if extension not in ['txt', 'exe', 'dll']:
        return result
    
    # If all conditions are met, return 'Yes'
    result = 'Yes'
    
    # Return the result
    return result