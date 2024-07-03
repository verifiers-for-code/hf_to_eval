from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize a stack to keep track of the opening parentheses
    stack = []

    # Initialize a variable to keep track of the start index of a group
    start_index = 0

    # Iterate through the characters in the input string
    for i, char in enumerate(paren_string):
        # If the character is an opening parenthesis, push its index onto the stack
        if char == '(':
            stack.append(i)
        # If the character is a closing parenthesis
        elif char == ')':
            # If the stack is not empty, pop the top index from the stack
            if stack:
                start_index = stack.pop()
            # If the stack is empty, the current group is not balanced
            else:
                break

    # If the stack is not empty, the input string is not balanced
    if stack:
        return []

    # Iterate through the characters in the input string again
    for i, char in enumerate(paren_string):
        # If the character is an opening parenthesis
        if char == '(':
            # If the stack is not empty, pop the top index from the stack
            if stack:
                start_index = stack.pop()
            # If the stack is empty, the current group is not balanced
            else:
                break
        # If the character is a closing parenthesis
        elif char == ')':
            # If the stack is not empty, pop the top index from the stack
            if stack:
                start_index = stack.pop()
            # If the stack is empty, the current group is balanced
            else:
                # Add the current group to the list of separate groups
                separate_groups.append(paren_string[start_index:i+1])
                # Reset the start index to the next character after the current group
                start_index = i+1

    # Return the list of separate groups
    return separate_groups