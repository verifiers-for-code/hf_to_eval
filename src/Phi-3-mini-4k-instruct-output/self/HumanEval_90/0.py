def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    

    Action Plan:
    1. Handle edge cases:
        a. Check for an empty list
        b. Check for a list with only one element
    
    2. Implement the function's main logic:
        a. Sort the list in ascending order while preserving the original indices
        b. Extract the second element from the sorted list, considering edge cases for indices
    
    3. Return the second smallest element or None if it does not exist"""
    
    # Step 1: Handle edge cases
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return None
    
    # Step 2: Implement the function's main logic
    sorted_lst = sorted(enumerate(lst), key=lambda x: x[1])
    second_smallest = None
    
    for i in range(len(sorted_lst)):
        if i == 0:
            continue
        if second_smallest is None:
            second_smallest = sorted_lst[i][1]
        else:
            break
    
    # Step 3: Return the second smallest element or None if it does not exist
    return second_smallest