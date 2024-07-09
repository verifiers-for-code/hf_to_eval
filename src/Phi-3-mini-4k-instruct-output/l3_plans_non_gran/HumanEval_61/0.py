def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    

    Action Plan:
    1. Initialize an empty stack to store opening brackets.
    2. Iterate through each character in the input string:
        a. If the character is an opening bracket '(':
            - Push the character onto the stack.
        b. If the character is a closing bracket ')':
            - Check if the stack is empty:
                - If empty, return False (no matching opening bracket).
            - Pop the top element from the stack.
    3. After processing the entire string:
        - Check if the stack is empty:
            - If empty, return True (all opening brackets have matching closing brackets).
            - If not empty, return False (some opening brackets do not have matching closing brackets)."""

    stack = []
    for char in brackets:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack