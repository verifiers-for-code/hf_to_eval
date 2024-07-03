def move_one_ball(arr):
    """
    Determines if it is possible to sort an array in non-decreasing order by performing right shift operations.

    Args:
    arr (list): A list of unique integers.

    Returns:
    bool: True if it is possible to sort the array, False otherwise.
    """
    # Step 1: Check if the input array is empty
    if not arr:
        return True

    # Step 2: Calculate the number of right shifts needed to sort the array
    max_element = max(arr)
    num_shifts = len(arr) - arr.index(max_element) - 1

    # Step 3: Check if the number of right shifts is possible
    if num_shifts > len(arr):
        return False

    # Step 4: Return True if the number of right shifts is possible, False otherwise
    return True