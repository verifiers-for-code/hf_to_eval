def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # Step 1: Initialize a variable to keep track of the count of consecutive spaces.
    consecutive_spaces_count = 0
    
    # Step 2: Iterate through the text with a loop.
    result = []
    for char in text:
        # Step 3: Check if the current character is a space and if the previous character was also a space.
        if char == ' ':
            consecutive_spaces_count += 1
            result.append(char)
        else:
            consecutive_spaces_count = 0
            result.append(char)
    
    # Step 4: Replace all spaces with '_' and check the count of consecutive spaces.
    modified_text = ''.join(result).replace(' ', '_')
    
    # Step 5: Replace all consecutive spaces with '-' if count is more than 2.
    if consecutive_spaces_count > 2:
        modified_text = modified_text.replace('  ', '-')
    
    # Step 6: Return the modified text.
    return modified_text