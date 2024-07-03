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
    # Step 2: Create a sorted version of the input list in ascending order
    ascending_sorted = sorted(l)

    # Step 3: Create another sorted version of the input list in descending order
    descending_sorted = sorted(l, reverse=True)

    # Step 4: Compare the original list with both sorted versions
    is_monotonic = (l == ascending_sorted) or (l == descending_sorted)

    # Step 5: Return True if the list is monotonic, False otherwise
    return is_monotonic