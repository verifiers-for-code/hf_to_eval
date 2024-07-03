def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']

    Action Plan:
    1. Initialize two variables to store the total character count for each list.
    2. Iterate through the first list (lst1):
       - For each string, add its length to the first count variable.
    3. Iterate through the second list (lst2):
       - For each string, add its length to the second count variable.
    4. Compare the two count variables:
       - If the first count is less than or equal to the second count, return lst1.
       - Otherwise, return lst2.

    Note: This plan ensures that if both lists have the same character count,
    the first list (lst1) will be returned as specified in the problem statement.
    '''
    count1 = sum(len(s) for s in lst1)
    count2 = sum(len(s) for s in lst2)

    if count1 <= count2:
        return lst1
    else:
        return lst2