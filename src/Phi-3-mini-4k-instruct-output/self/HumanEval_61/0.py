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
    1. Initialize a stack variable to track opening brackets:
        - As we iterate over the string, use the stack to keep track of opening brackets.
    
    2. Iterate over the input string character by character:
        - For each character, check if it's an opening bracket ('(')
    
    3. If the character is an opening bracket:
        - Push it onto the stack
    
    4. If the character is a closing bracket (')'):
        - Check if the stack is empty:
            - If yes, the string is incorrectly formatted, return False
        - If not, pop the last opening bracket from the stack
    
    5. After iterating over the string:
        - If the stack is empty, all brackets were correctly matched
        - If the stack is not empty, there are unmatched opening brackets, return False
    
    6. Return True indicating the string had correct bracketing
    
    7. Edge case handling:
        - Consider cases with consecutive brackets
        - Ensure handling of non-bracket characters without affecting the result"""

    stack = []
    for char in brackets:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return not stack