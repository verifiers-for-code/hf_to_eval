def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.

    Args:
    l (list): The input list to check for monotonicity.

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
    # Step 1: Check if the input list is empty
    if not l:
        return True

    # Step 2: Check if the list has only one element
    if len(l) == 1:
        return True

    # Step 3: Initialize a flag to track monotonicity
    is_monotonic = True

    # Step 4: Iterate through the list, comparing adjacent elements
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:  # Check for increasing monotonicity
            continue
        elif l[i] > l[i + 1]:  # Check for decreasing monotonicity
            continue
        else:
            is_monotonic = False
            break

    # Step 5: Return the flag
    return is_monotonic