def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    

    Action Plan:
    1. Initialize an empty stack to store opening brackets.
    2. Iterate through each character in the input string:
        a. If the character is an opening bracket ('<'), push it onto the stack.
        b. If the character is a closing bracket ('>'):
            - Check if the stack is empty (no matching opening bracket).
            - If the stack is not empty, pop the top element (the most recent opening bracket).
            - If the popped opening bracket does not match the current closing bracket, return False.
    3. After iterating through the entire string, check if the stack is empty:
        a. If the stack is empty, return True (all opening brackets have been matched).
        b. If the stack is not empty, return False (there are unmatched opening brackets)."""

    stack = []
    for char in brackets:
        if char == '<':
            stack.append(char)
        elif char == '>':
            if not stack:
                return False
            stack.pop()
    return not stack