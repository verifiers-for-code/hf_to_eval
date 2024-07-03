from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
    Action Plan:
    1. Initialize an empty list to store the final result
    2. Initialize an empty list or string to build the current group
    3. Initialize a counter to keep track of the current depth (nesting level) of parentheses
    4. Iterate through each character in the input string:
       a. If the character is '(', increment the depth and add it to the current group
       b. If the character is ')', decrement the depth and add it to the current group
       c. If the depth becomes 0 after processing a ')', it means a group is complete:
          - Add the current group to the result list
          - Reset the current group
    5. Return the result list containing all separated groups
    
    Note: Remember to ignore spaces in the input string during processing.
    """
    result = []
    current_group = ""
    depth = 0

    for char in paren_string.replace(" ", ""):
        if char == "(":
            depth += 1
            current_group += char
        elif char == ")":
            depth -= 1
            current_group += char
            if depth == 0:
                result.append(current_group)
                current_group = ""

    return result