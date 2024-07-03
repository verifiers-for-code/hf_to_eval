from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    

    Action Plan:
    1. Remove spaces from the input string to simplify processing.
    2. Initialize an empty stack to keep track of opening parentheses.
    3. Iterate through each character in the input string:
        a. If the character is an opening parenthesis ('('), push it onto the stack.
        b. If the character is a closing parenthesis (')'):
            - If the stack is empty, return an empty list (invalid input).
            - Pop the top element from the stack (an opening parenthesis).
            - If the popped element is not an opening parenthesis, return an empty list (invalid input).
    4. After processing all characters, if the stack is not empty, return an empty list (invalid input).
    5. Assemble the final result:
        a. Iterate through the stack, appending each opening parenthesis to a list.
        b. Return the list of strings, each representing a separate group of balanced parentheses.
    
    Note: Be careful when handling the stack and checking for balanced parentheses.
    Use a suitable data structure to implement the stack."""

    # Step 1: Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Step 2: Initialize an empty stack
    stack = []

    # Step 3: Iterate through each character in the input string
    for char in paren_string:
        if char == '(':
            # Push the opening parenthesis onto the stack
            stack.append(char)
        elif char == ')':
            # If the stack is empty, return an empty list (invalid input)
            if not stack:
                return []
            # Pop the top element from the stack
            top = stack.pop()
            # If the popped element is not an opening parenthesis, return an empty list (invalid input)
            if top != '(':
                return []

    # Step 4: After processing all characters, if the stack is not empty, return an empty list (invalid input)
    if stack:
        return []

    # Step 5: Assemble the final result
    result = []
    # Iterate through the stack, appending each opening parenthesis to a list
    while stack:
        result.append('(' + stack.pop() + ')')

    # Return the list of strings, each representing a separate group of balanced parentheses
    return result