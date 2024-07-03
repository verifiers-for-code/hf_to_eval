def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): The input list.

    Returns:
    bool: True if the list is monotonic, False otherwise.

    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Step 1: Define initial direction
    if len(l) < 2:
        return True  # An empty list or a list with only one element is considered monotonic

    direction = None
    for i in range(len(l) - 1):
        # Step 2: Iterate through the list
        current_direction = l[i] < l[i + 1]

        # Step 3: Handle edge cases
        if direction is None:
            direction = current_direction
        elif direction != current_direction:
            return False  # Direction changes, list is not monotonic

    return True  # If the loop completes without returning False, the list is monotonic