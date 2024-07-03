def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    Parameters:
    lst (list): A list of integers
    
    Returns:
    int or None: The 2nd smallest element in the list or None if there is no such element
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # Step 1: Check if the input list is empty
    if not lst:
        return None
    
    # Step 2: Find the smallest element in the list
    smallest = min(lst)
    
    # Step 3: Remove the smallest element from the list
    lst.remove(smallest)
    
    # Step 4: Check if the list still has elements
    if not lst:
        return None
    
    # Step 5: Find the second smallest element in the remaining list
    second_smallest = min(lst)
    
    return second_smallest