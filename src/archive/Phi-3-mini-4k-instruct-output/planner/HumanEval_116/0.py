def sort_array(arr):
    """
    Sorts an array of non-negative integers based on the number of ones in their binary representation in ascending order.
    For elements with the same number of ones, sorts them based on their decimal value.

    Args:
    arr (list): A list of non-negative integers.

    Returns:
    list: A sorted list of non-negative integers based on the specified criteria.

    Examples:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6])
    [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4])
    [0, 1, 2, 3, 4]
    """
    # Step 2: Create a custom sorting function
    sorted_arr = sorted(arr, key=lambda x: (bin(x).count('1'), x))

    return sorted_arr