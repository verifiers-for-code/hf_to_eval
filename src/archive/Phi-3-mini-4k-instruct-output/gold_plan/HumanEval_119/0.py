def is_balanced(s):
    """
    Helper function to check if a string of parentheses is balanced.
    """
    counter = 0
    for char in s:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
        if counter < 0:
            return False
    return counter == 0

def match_parens(lst):
    """
    Check if it's possible to concatenate two strings in some order to form a good string.
    """
    # Step 1: Concatenate the strings in both possible orders
    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]

    # Step 2: Check if either S1 or S2 is balanced
    if is_balanced(S1):
        return 'Yes'
    elif is_balanced(S2):
        return 'Yes'
    else:
        return 'No'