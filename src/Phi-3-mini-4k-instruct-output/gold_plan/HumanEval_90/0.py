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
    1. Remove duplicates from the input list
       - Hint: Use a built-in Python function to create a collection of unique elements
    
    2. Sort the list of unique elements in ascending order
       - Hint: Use a built-in Python function to sort the list
    
    3. Check if the sorted list of unique elements has at least 2 items
       - Hint: Use a conditional statement to check the length of the list
    
    4. If the list has at least 2 items:
       - Return the second element (index 1) of the sorted list
    
    5. If the list has fewer than 2 items:
       - Return None
    
    Note: Try to combine steps 1 and 2 into a single operation for efficiency
    """
    # Step 1: Remove duplicates and sort the list
    unique_sorted_lst = sorted(set(lst))
    
    # Step 3: Check if the list has at least 2 items
    if len(unique_sorted_lst) >= 2:
        # Step 4: Return the second element (index 1) of the sorted list
        return unique_sorted_lst[1]
    else:
        # Step 5: Return None
        return None