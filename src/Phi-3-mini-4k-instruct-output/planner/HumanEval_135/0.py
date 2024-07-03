def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    

    Action Plan:
    1. Initialize a variable `largest_index` to store the largest index of an element that is not greater than or equal to the element immediately preceding it. Set it to -1 initially.
    
    2. Iterate through the array starting from the second element (index 1) to the end.
    
    3. For each element, compare it with the element immediately preceding it (at index `i-1`).
    
    4. If the current element is not greater than or equal to the preceding element, update `largest_index` to the current index `i`.
    
    5. After iterating through the entire array, return `largest_index`.
    
    Note: Be careful when handling the edge case where the array has only one element."""
    
    largest_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            largest_index = i
    return largest_index