def incr_list(l: list):
    """
    Return a new list with elements incremented by 1.

    This function takes a list of integers as input and returns a new list where each element is incremented by 1.

    Parameters:
    l (list): A list of integers.

    Returns:
    list: A new list with elements incremented by 1.

    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    new_list = [x + 1 for x in l]
    return new_list