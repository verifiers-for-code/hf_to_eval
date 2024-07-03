def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    

    Action Plan:
    1. Check if the input list is empty:
        - If empty, return True (an empty list is considered monotonic)
    
    2. Check if the list has only one element:
        - If true, return True (a single element list is considered monotonic)
    
    3. Initialize a flag to track monotonicity:
        - Set it to True initially
    
    4. Iterate through the list, comparing adjacent elements:
        - For each pair of adjacent elements:
            a. Check if the current element is greater than the next element (for increasing monotonicity)
            b. Check if the current element is less than the next element (for decreasing monotonicity)
            c. If neither condition is met, set the flag to False (list is not monotonic)
    
    5. Return the flag:
        - If the flag is True, return True (list is monotonic)
        - If the flag is False, return False (list is not monotonic)
    
    Note: Be careful when handling edge cases and consider the definition of monotonicity."""
    if not l:
        return True
    if len(l) == 1:
        return True
    is_monotonic = True
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            continue
        elif l[i] > l[i + 1]:
            continue
        else:
            is_monotonic = False
            break
    return is_monotonic