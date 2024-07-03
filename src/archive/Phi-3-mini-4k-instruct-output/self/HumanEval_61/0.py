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
    # Step 1: Initialize a stack variable to track opening brackets
    stack = []

    # Step 2: Iterate over the input string character by character
    for char in brackets:
        # Step 3: If the character is an opening bracket, push it onto the stack
        if char == '(':
            stack.append(char)
        # Step 4: If the character is a closing bracket
        elif char == ')':
            # Step 5: Check if the stack is empty
            if not stack:
                return False
            # Step 6: Pop the last opening bracket from the stack
            stack.pop()

    # Step 7: After iterating over the string, check if the stack is empty
    return not stack