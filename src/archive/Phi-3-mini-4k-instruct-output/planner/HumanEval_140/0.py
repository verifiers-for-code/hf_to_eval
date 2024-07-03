def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    Parameters:
    text (str): The input string to be processed.
    
    Returns:
    str: The processed string with spaces replaced by underscores or dashes.
    
    Action Plan:
    1. Initialize an empty string to store the result.
    2. Iterate through each character in the input string:
        a. If the character is a space:
            - Check if the previous character is also a space.
            - If true, append a dash to the result string.
            - Otherwise, append an underscore to the result string.
        b. If the character is not a space, append it to the result string.
    3. Return the final result string.
    """
    result = ""
    consecutive_spaces = 0
    
    for char in text:
        if char == " ":
            if consecutive_spaces == 0:
                result += "_"
            else:
                result += "-"
            consecutive_spaces += 1
        else:
            result += char
            consecutive_spaces = 0
    
    return result