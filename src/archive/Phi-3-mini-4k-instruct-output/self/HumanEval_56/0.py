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
    """
    # Step 1: Initialize an empty stack or list to keep track of opening brackets.
    stack = []

    # Step 2: Iterate through each character in the input string.
    for bracket in brackets:
        # Step 2a: If a character is an opening bracket ("<"), add it to the stack.
        if bracket == "<":
            stack.append(bracket)
        # Step 2b: If a character is a closing bracket (">"), check if it corresponds to the last opening bracket.
        elif bracket == ">":
            # Step 2c: If the stack is empty or the corresponding opening bracket doesn't match, return False.
            if not stack or stack.pop() != "<":
                return False

    # Step 3: After the iteration, if the stack is empty, all brackets were properly matched and return True.
    return not stack