from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
    Action Plan:
    1. Split the input string into separate groups of parentheses.
    2. Create a helper function to process each group:
       a. Initialize variables to track current depth and maximum depth.
       b. Iterate through each character in the group:
          - If opening parenthesis, increase current depth and update max depth if needed.
          - If closing parenthesis, decrease current depth.
       c. Return the maximum depth reached for the group.
    3. Apply the helper function to each group in the input.
    4. Return a list of maximum depths for all groups.
    """
    # Split the input string into separate groups of parentheses
    groups = paren_string.split()

    # Helper function to process each group
    def process_group(group: str) -> int:
        current_depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Apply the helper function to each group in the input
    max_depths = [process_group(group) for group in groups]

    return max_depths