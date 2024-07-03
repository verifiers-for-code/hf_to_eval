def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Action Plan
    
    # 1. Define initial direction:
    if len(l) < 2:
        # Handle edge cases:
        # a. An empty list
        # b. A list with only one element
        return True
    
    direction = l[1] - l[0]
    increasing = direction > 0
    
    # 2. Iterate through the list:
    for i in range(2, len(l)):
        # b. Compare each element to the next
        if (l[i] - l[i-1]) * direction < 0:
            # Handle the case when the direction changes:
            # a. Return False immediately after the first change
            return False
    
    # 3. Handle edge cases:
    # c. A list with all equal elements
    if all(x == l[0] for x in l):
        return True
    
    # 4. Verify the monotonicity:
    # a. Ensure elements always follow the same direction (increase or decrease)
    # b. If the direction never changes, return True
    return True