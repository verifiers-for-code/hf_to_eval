def max_element(l: list):
    """
    Return the maximum element in the list.
    
    Parameters:
    l (list): A list of elements.
    
    Returns:
    int: The maximum element in the list.
    
    Example:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)