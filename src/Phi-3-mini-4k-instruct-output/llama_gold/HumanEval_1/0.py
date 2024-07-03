from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    

    Action Plan:
    1. Initialize an empty list to store the final result.
    2. Initialize an empty list to build the current parentheses group.
    3. Initialize a counter to track the depth of nested parentheses.
    4. Iterate through each character in the input string:
       a. If the character is an opening parenthesis '(':
          - Increment the depth counter
          - Add the character to the current group
       b. If the character is a closing parenthesis ')':
          - Decrement the depth counter
          - Add the character to the current group
          - If the depth counter reaches 0:
            * Join the characters in the current group into a string
            * Add this string to the result list
            * Clear the current group list
    5. Ignore any spaces in the input string during the iteration.
    6. Return the result list containing all separated parentheses groups."""

    result = []
    current_group = []
    depth = 0

    for char in paren_string:
        if char == ' ':
            continue
        elif char == '(':
            depth += 1
            current_group.append(char)
        elif char == ')':
            depth -= 1
            current_group.append(char)
            if depth == 0:
                result.append(''.join(current_group))
                current_group = []

    return result