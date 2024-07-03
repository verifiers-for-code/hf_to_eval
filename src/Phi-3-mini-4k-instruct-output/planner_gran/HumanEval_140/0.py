import re

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    

    1. Process the input string:
       - Store the input string in a variable (e.g., text)
    
    2. Replace spaces with underscores:
       - Use the string method replace() to replace all spaces in the string with underscores
       - Assign the result back to the text variable
    
    3. Handle consecutive spaces:
       - Split the modified string into a list of substrings using the split() method
       - Iterate through the list of substrings
       - Check if the length of the current substring is greater than 2
       - If true, replace the substring with a string containing a single underscore
       - If false, keep the original substring
       - Join the modified list of substrings back into a single string using the join() method
    
    4. Return the modified string:
       - Return the final processed string
    
    Additional implementation details:
    - Use the appropriate string methods for replacing spaces, splitting, and joining strings
    - Ensure that the function handles empty input strings correctly
    - Consider using a more efficient approach for handling consecutive spaces, such as using a regular expression"""
    
    # Step 1: Process the input string
    text = text
    
    # Step 2: Replace spaces with underscores
    text = text.replace(" ", "_")
    
    # Step 3: Handle consecutive spaces
    text = re.sub(r"(_+)(\s{2,})", r"\1-", text)
    
    # Step 4: Return the modified string
    return text