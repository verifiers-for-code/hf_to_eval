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
    1. Initialize a counter to track the depth of opening brackets.
    2. Iterate through each character in the input brackets string:
       a. If the character is an opening bracket "<", increment the depth counter.
       b. If the character is a closing bracket ">", decrement the depth counter.
       c. If the depth counter becomes negative at any point, immediately return False (indicating incorrect bracketing).
    3. After iterating through the entire string, check if the depth counter is 0.
       a. If it is, return True (indicating correct bracketing).
       b. If it's not, return False (indicating incorrect bracketing)."""

    depth = 0
    for char in brackets:
        if char == "<":
            depth += 1
        elif char == ">":
            depth -= 1
        if depth < 0:
            return False
    return depth == 0