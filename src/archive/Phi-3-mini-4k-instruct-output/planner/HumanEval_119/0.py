def match_parens(lst):
    """
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    """
    # Check if the first string has more closing parentheses than opening ones
    if lst[0].count(')') > lst[0].count('('):
        return 'No'
    
    # Check if the second string has more closing parentheses than opening ones
    if lst[1].count(')') > lst[1].count('('):
        return 'No'
    
    # Concatenate the two strings
    result = lst[0] + lst[1]
    
    # Check if the resulting string has balanced parentheses
    if result.count('(') == result.count(')'):
        return 'Yes'
    else:
        return 'No'