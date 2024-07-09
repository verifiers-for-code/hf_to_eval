from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    

    Action Plan:
    1. Remove spaces from the input string to ensure proper processing.
    2. Initialize an empty list to store the separated groups.
    3. Iterate through the input string, considering each character as a potential start of a group:
        a. Check if the current character is an opening parenthesis.
        b. If it is, check the following characters to form a group:
            - If the next character is a closing parenthesis, check if it matches the opening parenthesis.
            - If it matches, add the group to the list of separated groups and continue iterating.
        c. If the group is valid, skip the remaining characters in the string and move to the next group.
    4. Return the list of separated groups.
    
    Note: Implement a helper function to validate and separate groups of nested parentheses.
    Use a stack data structure to keep track of opening parentheses and match them with closing parentheses.
    Be careful when handling edge cases, such as empty input strings or strings with no groups."""

    def is_valid_group(group: str) -> bool:
        """ Helper function to validate a group of parentheses. """
        stack = []
        for char in group:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
        return not stack

    paren_string = paren_string.replace(' ', '')
    separated_groups = []
    start_index = 0

    while start_index < len(paren_string):
        end_index = paren_string.find(')', start_index)
        if end_index == -1:
            break
        group = paren_string[start_index:end_index + 1]
        if is_valid_group(group):
            separated_groups.append(group)
            start_index = end_index + 1
        else:
            start_index += 1

    return separated_groups