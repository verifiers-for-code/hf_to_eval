def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    """
    # Replace all spaces with underscores
    text = text.replace(" ", "_")
    
    # Replace more than 2 consecutive spaces with -
    while "   " in text:
        text = text.replace("   ", "-")
    
    return text