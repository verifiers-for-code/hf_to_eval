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
    """

    # Action Plan
    # 1. Initialize a stack variable to track opening brackets
    stack = []

    # 2. Iterate over the input string character by character
    for char in brackets:
        # 3. If the character is an opening bracket
        if char == '(':
            # Push it onto the stack
            stack.append(char)
        # 4. If the character is a closing bracket
        elif char == ')':
            # Check if the stack is empty
            if not stack:
                # The string is incorrectly formatted, return False
                return False
            # Pop the last opening bracket from the stack
            stack.pop()

    # 5. After iterating over the string
    # If the stack is empty, all brackets were correctly matched
    # If the stack is not empty, there are unmatched opening brackets, return False
    return not stack