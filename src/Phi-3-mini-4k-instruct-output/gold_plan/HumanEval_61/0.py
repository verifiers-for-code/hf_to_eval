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
    1. Initialize a counter variable to keep track of open brackets.
    2. Iterate through each character in the 'brackets' string:
       a. If the character is an opening bracket "(", increment the counter.
       b. If the character is a closing bracket ")", decrement the counter.
       c. If at any point the counter becomes negative, return False
          (this means a closing bracket appeared before its corresponding opening bracket).
    3. After the iteration, check if the counter is zero:
       a. If it's zero, return True (all brackets are properly matched).
       b. If it's not zero, return False (there are unmatched opening brackets).
    """
    counter = 0
    for char in brackets:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0