from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a separate group of balanced parentheses.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Step 1: Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Step 2: Initialize an empty stack to keep track of opening parentheses
    stack = []

    # Step 3: Iterate through each character in the input string
    result = []
    current_group = ""
    for char in paren_string:
        if char == "(":
            # Step 3a: Push opening parenthesis onto the stack
            stack.append(char)
        elif char == ")":
            # Step 3b: Check if the stack is empty or the top element is not an opening parenthesis
            if not stack or stack[-1] != "(":
                return []
            # Pop the top element from the stack
            stack.pop()
            # If the stack is empty, we have found a complete group
            if not stack:
                result.append(current_group)
                current_group = ""
        else:
            # Append non-parenthesis characters to the current group
            current_group += char

    # Step 4: Check if the stack is empty after processing all characters
    if stack:
        return []

    # Step 5: Assemble the final result
    return result