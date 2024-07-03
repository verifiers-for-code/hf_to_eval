def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    l (list): A list of integers.
    
    Returns:
    int: The maximum element in the list.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Step 2: Initialize a variable to store the maximum element.
    # Set it to the first element of the list by default.
    if not l:  # Step 6: Handle edge case of an empty list
        return None
    max_element = l[0]
    
    # Step 3: Iterate over the list using a loop, comparing each element to the current maximum element.
    for element in l[1:]:  # Start from the second element
        if element > max_element:
            max_element = element
    
    # Step 5: After the loop completes, return the maximum element.
    return max_element