def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.

    Args:
    l (list): A list of integers.
    t (int): A threshold value.

    Returns:
    bool: True if all numbers in the list l are below threshold t, False otherwise.

    Examples:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # Iterate over the list and check if any number is above the threshold
    for num in l:
        if num >= t:
            return False
    return True