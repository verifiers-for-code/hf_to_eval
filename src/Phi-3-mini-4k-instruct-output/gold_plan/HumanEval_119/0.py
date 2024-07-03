def match_parens(lst):
    '''
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

    Action Plan:
    1. Define a helper function 'is_balanced(s)' that checks if a string of parentheses is balanced:
       a. Initialize a counter variable to 0
       b. Iterate through each character in the string:
          - If it's '(', increment the counter
          - If it's ')', decrement the counter
          - If the counter ever becomes negative, return False
       c. After the loop, return True if the counter is 0, False otherwise

    2. In the main function:
       a. Create two strings by concatenating the input strings in both possible orders:
          S1 = lst[0] + lst[1]
          S2 = lst[1] + lst[0]

    3. Check both S1 and S2 using the is_balanced function

    4. Return 'Yes' if either S1 or S2 is balanced, 'No' otherwise
    '''

    def is_balanced(s):
        counter = 0
        for char in s:
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]

    if is_balanced(S1) or is_balanced(S2):
        return 'Yes'
    else:
        return 'No'