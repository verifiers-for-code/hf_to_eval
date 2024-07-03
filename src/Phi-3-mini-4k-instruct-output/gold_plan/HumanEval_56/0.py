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
    1. Initialize a variable to keep track of the bracket nesting level (let's call it 'depth').
    2. Iterate through each character in the 'brackets' string:
       a. If the character is an opening bracket '<':
          - Increment the depth
       b. If the character is a closing bracket '>':
          - Decrement the depth
       c. After each change to depth, check if it has become negative:
          - If so, return False immediately (closing bracket without an opening)
    3. After the loop, check if the final depth is zero:
       - If it is, return True (all brackets are properly closed)
       - If not, return False (some opening brackets were not closed)
    """
    depth = 0
    for char in brackets:
        if char == '<':
            depth += 1
        elif char == '>':
            depth -= 1
            if depth < 0:
                return False
    return depth == 0