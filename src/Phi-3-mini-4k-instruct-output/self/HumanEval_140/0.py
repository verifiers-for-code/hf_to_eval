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
    1. Initialize a variable to keep track of the count of consecutive spaces.
    2. Iterate through the text with a loop.
    3. In each iteration, check if the current character is a space and if the previous character was also a space.
        - If so, increment the count of consecutive spaces.
        - Otherwise, reset the count of consecutive spaces.
    4. After the loop, check the count:
        - If it is more than 2, replace all consecutive spaces in the text with '-'
        - Otherwise, replace all spaces with '_'
    
    5. Return the modified text
    
    6. Consider edge cases such as:
        - An empty string (return it without modification)
        - A string with no spaces (return the original string)
    
    7. Optimize by running the consecutive spaces check only once after the space replacements."""
    
    # Step 1: Initialize a variable to keep track of the count of consecutive spaces.
    consecutive_spaces = 0
    
    # Step 2: Iterate through the text with a loop.
    result = []
    for char in text:
        # Step 3: Check if the current character is a space and if the previous character was also a space.
        if char == ' ':
            if result and result[-1] == ' ':
                consecutive_spaces += 1
            else:
                consecutive_spaces = 1
        else:
            consecutive_spaces = 0
        
        # Step 4: After the loop, check the count.
        if consecutive_spaces > 2:
            result.append('-')
        else:
            result.append('_')
    
    # Step 5: Return the modified text
    return ''.join(result)