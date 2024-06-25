def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    """
    result = ""
    consecutive_spaces = 0
    
    for char in text:
        if char == " ":
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                result += "-"
            else:
                result += "_"
        else:
            consecutive_spaces = 0
            result += char
            
    return result