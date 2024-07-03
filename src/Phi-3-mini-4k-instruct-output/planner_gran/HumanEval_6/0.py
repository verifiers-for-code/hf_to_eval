from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    

    1. Split the input string into a list of groups:
       - Use the split() method with a space as the separator to divide the string into individual groups
    
    2. Define a helper function to count the maximum depth of nested parentheses in a group:
       a. Initialize a counter for the current depth
       b. Iterate through each character in the group:
          - If the character is an opening parenthesis, increment the depth counter
          - If the character is a closing parenthesis, decrement the depth counter
          - Update the maximum depth if the current depth is greater
       c. Return the maximum depth found in the group
    
    3. Initialize an empty list to store the maximum depths:
       - This list will hold the maximum depths for each group of parentheses
    
    4. Iterate over each group in the list of groups:
       a. Call the helper function to count the maximum depth of nested parentheses in the current group
       b. Append the maximum depth to the list of maximum depths
    
    5. Return the list of maximum depths:
       - This list contains the deepest level of nesting for each group of parentheses
    
    Additional implementation details:
    - Use a conditional statement to check if the character is an opening or closing parenthesis
    - Use a variable to keep track of the maximum depth found so far
    - Ensure that the function handles empty input strings and groups correctly
    - Consider adding error handling for invalid input formats"""

    # Split the input string into a list of groups
    groups = paren_string.split()

    # Define a helper function to count the maximum depth of nested parentheses in a group
    def count_max_depth(group: str) -> int:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    # Initialize an empty list to store the maximum depths
    max_depths = []

    # Iterate over each group in the list of groups
    for group in groups:
        # Call the helper function to count the maximum depth of nested parentheses in the current group
        max_depth = count_max_depth(group)
        # Append the maximum depth to the list of maximum depths
        max_depths.append(max_depth)

    # Return the list of maximum depths
    return max_depths