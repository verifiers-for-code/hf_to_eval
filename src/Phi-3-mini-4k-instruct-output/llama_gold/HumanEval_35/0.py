def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    

    Action Plan:
    1. Initialize the maximum element with the first element of the input list.
    2. Iterate through each element in the input list:
       a. Compare the current element with the current maximum element.
       b. If the current element is greater than the maximum element, update the maximum element with the current element.
    3. After iterating through the entire list, the maximum element will be the largest element in the list.
    4. Return the maximum element."""
    
    # Step 1: Initialize the maximum element with the first element of the input list
    max_element = l[0]
    
    # Step 2: Iterate through each element in the input list
    for element in l:
        # Step 2a: Compare the current element with the current maximum element
        if element > max_element:
            # Step 2b: If the current element is greater than the maximum element, update the maximum element with the current element
            max_element = element
    
    # Step 3: After iterating through the entire list, the maximum element will be the largest element in the list
    
    # Step 4: Return the maximum element
    return max_element