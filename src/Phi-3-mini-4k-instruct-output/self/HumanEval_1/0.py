from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    

    Action Plan:
    1. Initial Preprocessing:
        a. Remove all spaces from the input string
    
    2. Stack-based Parentheses Tracking:
        a. Iterate through each character in the string
        b. For every opening parenthesis, push it onto the stack
        c. For every closing parenthesis, pop from the stack
        d. Use a list to store the strings within each separate group
    
    3. Handling Separation:
        a. When the stack is empty (and there are no more closing parentheses), it indicates the start of a new group
        b. Add the characters from the input string to the current list until the stack is not empty (a closing parenthesis is encountered)
        c. Once a new group starts, reset the current list and continue the process
    
    4. Edge Cases Handling:
        a. Ignore the strings with unbalanced parentheses
        b. Ignore strings with nested parentheses
    
    5. Returning the results:
        a. After processing the entire string, return the list of separate strings representing the groups
    
    6. Optimization Considerations:
        a. Use efficient string concatenation methods
        b. Process the string in a single pass to ensure time efficiency"""

    # Initial Preprocessing: Remove all spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Stack-based Parentheses Tracking
    stack = []
    current_group = []
    result = []

    for char in paren_string:
        if char == "(":
            stack.append(char)
            current_group.append(char)
        elif char == ")":
            if stack:
                stack.pop()
                current_group.append(char)
            else:
                # Ignore unbalanced parentheses
                continue

        # Handling Separation
        if not stack:
            # When the stack is empty, it indicates the start of a new group
            result.append("".join(current_group))
            current_group = []

    # Returning the results
    return result