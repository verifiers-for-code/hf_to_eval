def unique(l: list):
    """Return sorted unique elements in a list

    Args:
    l (list): A list of elements

    Returns:
    list: A sorted list of unique elements

    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_elements = set(l)
    
    # Convert the set back to a list and sort it
    sorted_unique_elements = sorted(list(unique_elements))
    
    return sorted_unique_elements