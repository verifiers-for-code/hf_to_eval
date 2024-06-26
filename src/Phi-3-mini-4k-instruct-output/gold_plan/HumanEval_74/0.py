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
    '''
    # Step 1: Initialize two variables to store the total character count for each list.
    count1 = sum(len(s) for s in lst1)
    count2 = sum(len(s) for s in lst2)

    # Step 2 and 3: Iterate through the lists and calculate the total character count.
    # Step 4: Compare the two count variables and return the appropriate list.
    if count1 <= count2:
        return lst1
    else:
        return lst2