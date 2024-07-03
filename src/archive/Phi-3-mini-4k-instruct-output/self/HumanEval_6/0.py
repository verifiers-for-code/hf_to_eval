from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    # Step 1: Tokenize the input string by spaces to separate groups of nested parentheses.
    groups = paren_string.split()

    def calculate_nesting_depth(group: str) -> int:
        # Step 2: Develop a method to calculate the nesting depth of a group.
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
                if depth < 0:
                    raise ValueError("Unbalanced parentheses in group: " + group)
        return max_depth

    # Step 3: Iterate through the list of groups and apply the nesting depth calculation method to each group.
    nesting_depths = [calculate_nesting_depth(group) for group in groups]

    # Step 4: Return the list of nesting depths.
    return nesting_depths