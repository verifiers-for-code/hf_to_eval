def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    

    Action Plan:
    1. Initialize an empty string to store the modified text.
    2. Iterate through each character in the input text:
        a. If the character is a space:
            - If the previous character is also a space, append a hyphen to the modified text.
            - If the previous character is not a space, append an underscore to the modified text.
        b. If the character is not a space, append it to the modified text.
    3. Return the modified text.
    
    Note: Use a loop to iterate through the characters in the input text.
    Be careful to handle consecutive spaces correctly.
    Use string methods to manipulate the characters and build the modified text."""
    
    modified_text = ""
    prev_char = ""
    
    for char in text:
        if char == " ":
            if prev_char == " ":
                modified_text += "-"
            else:
                modified_text += "_"
        else:
            modified_text += char
        prev_char = char
    
    return modified_text