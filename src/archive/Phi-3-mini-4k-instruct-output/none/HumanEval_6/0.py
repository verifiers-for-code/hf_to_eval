from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Split the input string into groups of nested parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the deepest level of nesting for each group
    deepest_levels = []

    for group in groups:
        # Initialize a counter to keep track of the current level of nesting
        level = 0

        # Iterate through each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the level counter
            if char == '(':
                level += 1
            # If the character is a closing parenthesis, decrement the level counter
            elif char == ')':
                level -= 1

        # Append the deepest level of nesting for the current group to the list
        deepest_levels.append(level)

    return deepest_levels