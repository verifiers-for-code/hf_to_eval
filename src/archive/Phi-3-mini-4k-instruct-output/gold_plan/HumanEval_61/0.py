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
    # Step 1: Initialize a counter variable to keep track of open brackets.
    open_brackets_counter = 0

    # Step 2: Iterate through each character in the 'brackets' string.
    for bracket in brackets:
        # a. If the character is an opening bracket "(", increment the counter.
        if bracket == "(":
            open_brackets_counter += 1
        # b. If the character is a closing bracket ")", decrement the counter.
        elif bracket == ")":
            open_brackets_counter -= 1
        # c. If at any point the counter becomes negative, return False.
        if open_brackets_counter < 0:
            return False

    # Step 3: After the iteration, check if the counter is zero.
    # a. If it's zero, return True (all brackets are properly matched).
    if open_brackets_counter == 0:
        return True
    # b. If it's not zero, return False (there are unmatched opening brackets).
    else:
        return False