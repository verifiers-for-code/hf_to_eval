def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Args:
    arr (list): A list of integers without duplicates.

    Returns:
    int: The largest index of an element that is not greater than or equal to the element immediately preceding it, or -1 if no such element exists.

    Action Plan:
    1. Initialize a variable `largest_index` to store the largest index of an element that is not greater than or equal to the element immediately preceding it. Set it to -1 initially.
    2. Iterate through the array starting from the second element (index 1) to the end.
    3. For each element, compare it with the element immediately preceding it (at index `i-1`).
    4. If the current element is not greater than or equal to the preceding element, update `largest_index` to the current index `i`.
    5. After iterating through the entire array, return `largest_index`.
    6. Handle the edge case where the array has only one element.
    """
    largest_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            largest_index = i
    return largest_index