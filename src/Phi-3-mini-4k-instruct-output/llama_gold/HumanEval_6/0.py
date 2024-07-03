from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    

    Action Plan:
    1. Split the input string into individual groups of parentheses using the space character as a separator.
    2. For each group, initialize two counters: current_depth and max_depth, both set to 0.
    3. Iterate through each character in the group:
       a. If the character is an opening parenthesis '(':
          - Increment the current_depth counter
          - Update max_depth if current_depth is greater
       b. If the character is a closing parenthesis ')':
          - Decrement the current_depth counter
    4. After processing each group, add the max_depth to the result list.
    5. Return the list of maximum depths for all groups."""

    result = []
    groups = paren_string.split()

    for group in groups:
        current_depth = 0
        max_depth = 0

        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        result.append(max_depth)

    return result