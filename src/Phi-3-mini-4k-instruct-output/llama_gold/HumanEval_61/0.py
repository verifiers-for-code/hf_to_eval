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
    1. Initialize a counter (depth) to 0, which will track the balance of opening and closing brackets.
    2. Iterate through each character in the input string:
       a. If the character is an opening bracket '(':
          - Increment the depth counter
       b. If the character is a closing bracket ')':
          - Decrement the depth counter
          - If the depth counter becomes negative, return False (invalid bracket sequence)
    3. After iterating through the entire string:
       a. If the depth counter is 0, return True (correct bracketing)
       b. If the depth counter is not 0, return False (incorrect bracketing)"""

    depth = 0
    for char in brackets:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0