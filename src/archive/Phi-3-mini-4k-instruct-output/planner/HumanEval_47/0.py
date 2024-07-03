def median(l: list) -> float:
    """
    Return median of elements in the list l.
    
    Args:
    l (list): A list of numeric elements.
    
    Returns:
    float: The median value of the elements in the list.
    
    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    10.0
    """
    # Step 1: Sort the input list in ascending order using the built-in sorted() function
    sorted_list = sorted(l)
    
    # Step 2: Determine the length of the sorted list
    n = len(sorted_list)
    
    # Step 3: Check if the length of the list is even or odd
    if n % 2 == 0:
        # If even:
        # Calculate the median as the average of the two middle elements
        median_value = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
    else:
        # If odd:
        # Calculate the median as the middle element
        median_value = sorted_list[n//2]
    
    # Step 4: Return the calculated median value
    return median_value