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
    # Initialize a counter to keep track of the brackets
    bracket_counter = 0

    # Iterate through the string
    for bracket in brackets:
        if bracket == "(":
            # Increment the counter for an opening bracket
            bracket_counter += 1
        elif bracket == ")":
            # Decrement the counter for a closing bracket
            bracket_counter -= 1

        # If the counter becomes negative, it means there's a closing bracket without an opening one
        if bracket_counter < 0:
            return False

    # If the counter is 0, it means all opening brackets have a corresponding closing bracket
    return bracket_counter == 0