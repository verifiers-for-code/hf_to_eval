from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    

    Action Plan:
    1. Define a function `parse_nested_parens` that takes a string `paren_string` as input.
    2. Initialize an empty list `nesting_levels` to store the deepest level of nesting for each group.
    3. Iterate through each group in the input string:
        a. Initialize a counter `nesting_level` to 0.
        b. Initialize a flag `is_nested` to True.
        c. Iterate through each character in the current group:
            - If the character is an opening parenthesis, increment `nesting_level` and `is_nested`.
            - If the character is a closing parenthesis, decrement `nesting_level`.
            - If `nesting_level` becomes negative, set `is_nested` to False and break the loop.
        d. If `is_nested` is True, append the maximum `nesting_level` to `nesting_levels`.
    4. Return the `nesting_levels` list containing the deepest level of nesting for each group.
    5. Consider using a recursive function to calculate the deepest level of nesting for each group."""

    def get_max_nesting_level(group: str) -> int:
        nesting_level = 0
        is_nested = True
        for char in group:
            if char == '(':
                nesting_level += 1
                is_nested = True
            elif char == ')':
                nesting_level -= 1
                if nesting_level < 0:
                    is_nested = False
                    break
        return max(nesting_level, 0) if is_nested else 0

    groups = paren_string.split()
    nesting_levels = [get_max_nesting_level(group) for group in groups]
    return nesting_levels