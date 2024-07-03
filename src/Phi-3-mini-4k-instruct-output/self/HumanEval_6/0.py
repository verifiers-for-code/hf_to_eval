from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    

    Action Plan:
    1. Tokenize the input string by spaces to separate groups of nested parentheses.
    2. Develop a method to calculate the nesting depth of a group:
        a. Initialize a depth counter
        b. Iterate through each character in the group
        c. Increment the counter for each '(' encountered and decrement it for each ')' encountered
        d. Keep track of the maximum depth encountered during the iteration
    3. Iterate through the list of groups and apply the nesting depth calculation method to each group.
        a. Call the method defined in step 2 for each group
        b. Store the results in a new list
    4. Return the list of nesting depths.
    
    5. Handle edge cases:
        a. Empty string
        b. Groups with no parentheses
        c. Groups with unbalanced parentheses
    
    6. Additional considerations for optimization:
        a. Early termination in the calculation method when the counter goes below zero, indicating unbalanced parentheses"""

    def calculate_depth(group: str) -> int:
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
                if depth < 0:
                    return 0  # Unbalanced parentheses
        return max_depth

    groups = paren_string.split()
    depths = [calculate_depth(group) for group in groups]
    return depths