from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Step 1: Initial Preprocessing
    paren_string = paren_string.replace(" ", "")

    stack = []
    current_group = []
    result = []

    # Step 2: Stack-based Parentheses Tracking
    for char in paren_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
                if not stack:
                    # Step 3: Handling Separation
                    current_group.append(char)
                    result.append("".join(current_group))
                    current_group = []
            else:
                # Edge Case Handling: Ignore unbalanced parentheses
                pass

    # Step 4: Returning the results
    return result