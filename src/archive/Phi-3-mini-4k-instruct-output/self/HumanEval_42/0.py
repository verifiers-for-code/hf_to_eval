def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # Step 1: Initialize a new list to hold the incremented values using list comprehension
    incremented_list = [x + 1 for x in l]
    
    # Step 2: Loop through each element in the input list (not needed as we are using list comprehension)
    
    # Step 3: Add 1 to the current element in the loop to obtain the incremented value
    # (Already done in the list comprehension step)
    
    # Step 4: Append the incremented value to the new list
    # (Already done in the list comprehension step)
    
    # Step 5: Return the newly created list
    return incremented_list