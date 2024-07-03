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
    1. Initialize an empty string to store the result.
    2. Iterate through each character in the input string:
        a. If the character is a space:
            - Check if the previous character is also a space.
            - If true, append a dash to the result string.
            - Otherwise, append an underscore to the result string.
        b. If the character is not a space, append it to the result string.
    3. Return the final result string.
    
    Note: Be careful when handling consecutive spaces and replacing them with a dash.
    Use appropriate string methods for concatenation and replacement."""
    
    result = ""
    prev_char = ""
    for char in text:
        if char == " ":
            if prev_char == " ":
                result += "-"
            else:
                result += "_"
        else:
            result += char
        prev_char = char
    return result