from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def calculate_nesting_depth(group: str) -> int:
        """
        Calculate the nesting depth of a group of parentheses.
        """
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    # Tokenize the input string by spaces to separate groups of nested parentheses
    groups = paren_string.split()

    # Iterate through the list of groups and apply the nesting depth calculation method to each group
    nesting_depths = [calculate_nesting_depth(group) for group in groups]

    return nesting_depths