from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]

    Action Plan:
    1. Split the input string into groups of nested parentheses using spaces as separators.
    2. Initialize an empty stack to keep track of the nesting levels.
    3. Iterate through each character in the input string:
        a. If the character is an opening parenthesis '(', push its index onto the stack.
        b. If the character is a closing parenthesis ')', pop the top index from the stack.
        c. Calculate the current nesting level by subtracting the top index from the current index.
        d. Update the maximum nesting level if the current level is greater.
    4. After iterating through the entire string, return the list of maximum nesting levels.
    
    Note: Use a stack to keep track of the nesting levels and update the maximum level accordingly.
    Be careful when handling opening and closing parentheses to avoid index errors."""
    
    # Split the input string into groups of nested parentheses using spaces as separators
    groups = paren_string.split()
    
    # Initialize an empty stack to keep track of the nesting levels
    stack = []
    
    # Initialize a variable to keep track of the maximum nesting level
    max_nesting_level = 0
    
    # List to store the maximum nesting levels for each group
    max_nesting_levels = []
    
    # Iterate through each character in the input string
    for i, char in enumerate(paren_string):
        # If the character is an opening parenthesis '(', push its index onto the stack
        if char == '(':
            stack.append(i)
        # If the character is a closing parenthesis ')', pop the top index from the stack
        elif char == ')':
            if stack:
                top_index = stack.pop()
                # Calculate the current nesting level by subtracting the top index from the current index
                current_nesting_level = i - top_index
                # Update the maximum nesting level if the current level is greater
                if current_nesting_level > max_nesting_level:
                    max_nesting_level = current_nesting_level
            else:
                raise ValueError("Unmatched closing parenthesis at index {}".format(i))
    
    # After iterating through the entire string, append the maximum nesting level to the list
    for group in groups:
        max_nesting_levels.append(max_nesting_level)
    
    return max_nesting_levels