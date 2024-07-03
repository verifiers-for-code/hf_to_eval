from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    

    1. Initialize an empty stack to store opening parentheses
       - This stack will be used to keep track of the opening parentheses encountered so far
    
    2. Initialize an empty list to store the separate groups
       - This list will hold the separated groups of parentheses
    
    3. Initialize an empty string to store the current group
       - This string will be used to build the current group of parentheses
    
    4. Iterate through each character in the input string:
       a. If the character is an opening parenthesis '(':
          - Push the opening parenthesis onto the stack
       b. If the character is a closing parenthesis ')':
          - Check if the stack is empty:
             - If empty, skip to the next character (no matching opening parenthesis)
          - Pop the top element from the stack (matching opening parenthesis)
          - Check if the stack is empty again:
             - If empty, add the current group to the list of separate groups
          - Add the closing parenthesis to the current group
       c. If the character is a space:
          - Skip to the next character (ignore spaces)
    
    5. After iterating through the entire string:
       - Add the remaining group to the list of separate groups
    
    6. Return the list of separate groups
    
    Additional implementation details:
    - Use a list to implement the stack for opening parentheses
    - Use a string to build the current group of parentheses
    - Use a list to store the separate groups
    - Ensure that the function handles empty input strings correctly
    - Consider using a try-except block to handle potential errors (e.g., non-string input)"""
    
    stack = []
    separate_groups = []
    current_group = ""
    
    for char in paren_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                continue
            stack.pop()
            if not stack:
                separate_groups.append(current_group)
                current_group = ""
            else:
                current_group += char
        elif char == " ":
            continue
    
    if current_group:
        separate_groups.append(current_group)
    
    return separate_groups