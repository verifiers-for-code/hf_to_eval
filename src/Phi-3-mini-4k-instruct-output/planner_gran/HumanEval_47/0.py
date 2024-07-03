def median(l: list):
    """
    Return median of elements in the list l.
    
    Parameters:
    l (list): A list of numbers.
    
    Returns:
    float: The median of the list.
    
    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    
    # Handle edge cases
    if not l:
        raise ValueError("Input list is empty")
    
    # Sort the input list in ascending order
    try:
        sorted_list = sorted(l)
    except TypeError:
        raise TypeError("Input list contains non-numeric values")
    
    # Calculate the median based on the list's length
    n = len(sorted_list)
    if n % 2 == 0:
        # If even, the median is the average of the two middle elements
        median_value = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
    else:
        # If odd, the median is the middle element
        median_value = sorted_list[n//2]
    
    return median_value