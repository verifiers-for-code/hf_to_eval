def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    

    Action Plan:
    1. Initialize an empty list to store the incremented elements.
    2. Iterate through each element in the input list:
       a. Increment the element by 1.
       b. Add the incremented element to the new list.
    3. Return the new list containing the incremented elements."""
    
    # Step 1: Initialize an empty list to store the incremented elements
    incremented_list = []
    
    # Step 2: Iterate through each element in the input list
    for element in l:
        # Step 2a: Increment the element by 1
        incremented_element = element + 1
        
        # Step 2b: Add the incremented element to the new list
        incremented_list.append(incremented_element)
    
    # Step 3: Return the new list containing the incremented elements
    return incremented_list