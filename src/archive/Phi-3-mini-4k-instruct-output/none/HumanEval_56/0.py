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
    # Initialize a counter to keep track of the balance of brackets
    balance = 0

    # Iterate through the string
    for bracket in brackets:
        # If the bracket is an opening bracket, increment the balance
        if bracket == "<":
            balance += 1
        # If the bracket is a closing bracket, decrement the balance
        elif bracket == ">":
            balance -= 1

        # If the balance becomes negative at any point, return False
        if balance < 0:
            return False

    # If the balance is 0 at the end, return True, else return False
    return balance == 0