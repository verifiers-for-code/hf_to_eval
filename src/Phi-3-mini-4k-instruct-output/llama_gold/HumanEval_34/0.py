def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    

    Action Plan:
    1. Convert the input list into a data structure that automatically removes duplicates (e.g., a set).
    2. Convert the resulting data structure back into a list.
    3. Sort the list in ascending order.
    4. Return the sorted list containing only unique elements."""
    
    # Step 1: Convert the input list into a set to remove duplicates
    unique_set = set(l)
    
    # Step 2: Convert the set back into a list
    unique_list = list(unique_set)
    
    # Step 3: Sort the list in ascending order
    unique_list.sort()
    
    # Step 4: Return the sorted list containing only unique elements
    return unique_list