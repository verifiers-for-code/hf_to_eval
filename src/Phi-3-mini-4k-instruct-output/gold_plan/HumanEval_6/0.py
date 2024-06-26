from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    # Step 1: Split the input string into separate groups of parentheses
    groups = paren_string.split()

    def process_group(group: str) -> int:
        # Step 2: Helper function to process each group
        current_depth = 0
        max_depth = 0

        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        return max_depth

    # Step 3: Apply the helper function to each group in the input
    depths = [process_group(group) for group in groups]

    # Step 4: Return a list of maximum depths for all groups
    return depths