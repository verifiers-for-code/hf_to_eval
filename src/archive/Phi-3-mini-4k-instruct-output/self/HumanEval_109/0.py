def move_one_ball(arr):
    """Determine if it is possible to sort an array in non-decreasing order by performing right shift operations."""
    
    # Helper function to perform a right shift operation on an array
    def right_shift(arr):
        last_element = arr.pop()
        arr.insert(0, last_element)
        return arr

    # Edge cases
    if not arr:
        return True
    if len(arr) == 1:
        return True
    if arr == sorted(arr):
        return True

    # Check if sorting is possible with the right shift operation
    sorted_arr = sorted(arr)
    while arr != sorted_arr:
        arr = right_shift(arr)
        if arr == sorted_arr:
            return True
        if arr[0] > arr[-1]:
            return False

    return False