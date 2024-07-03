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
    1. Initialize variables:
       - Create an empty string to store the result
       - Set up counters to keep track of the current position and space sequences
    
    2. Iterate through each character in the input text:
       - Use a while loop to go through the string
    
    3. For each character, check if it's a space:
       - If it is a space, increment the space counter
       - If it's not a space, process the preceding spaces (if any):
         a. If more than 2 consecutive spaces, add a hyphen
         b. If 1-2 spaces, add underscore(s)
         c. If no spaces, just add the character
       - Reset the space counters after processing
    
    4. After the loop, handle any trailing spaces:
       - Use the same logic as in step 3
    
    5. Return the resulting string with replaced spaces
    """
    result = ""
    space_counter = 0
    i = 0
    while i < len(text):
        if text[i] == " ":
            space_counter += 1
        else:
            if space_counter > 2:
                result += "-"
            elif space_counter > 0:
                result += "_" * space_counter
            result += text[i]
            space_counter = 0
        i += 1
    
    # Handle trailing spaces
    if space_counter > 0:
        if space_counter > 2:
            result += "-"
        elif space_counter > 0:
            result += "_" * space_counter
    
    return result