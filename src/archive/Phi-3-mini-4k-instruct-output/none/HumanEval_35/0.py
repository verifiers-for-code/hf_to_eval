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
    # Check if the list is empty
    if not l:
        return "List is empty"

    # Initialize the maximum element with the first element of the list
    max_element = l[0]

    # Iterate through the list and update the maximum element
    for element in l:
        if element > max_element:
            max_element = element

    return max_element