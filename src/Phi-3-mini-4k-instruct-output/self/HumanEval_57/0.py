def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Action Plan:
    1. Define initial direction:
        a. Initialize variables for checking increasing or decreasing
        b. Determine initial direction based on the first two elements
    
    2. Iterate through the list:
        a. Compare each element to the next
        b. If the comparison result changes, the list is not monotonic
    
    3. Handle edge cases:
        a. An empty list
        b. A list with only one element
        c. A list with all equal elements
    
    4. Verify the monotonicity:
        a. Ensure elements always follow the same direction (increase or decrease)
        b. If the direction never changes, return True
    
    5. Handle the case when the direction changes:
        a. Return False immediately after the first change
        b. If the end of the list is reached, return False since the list isn't strictly monotonic
    
    6. Optimize the loop to avoid unnecessary comparisons if possible
    """
    if len(l) < 2:
        return True
    
    direction = None
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            if direction == "decreasing":
                return False
            direction = "increasing"
        elif l[i] > l[i + 1]:
            if direction == "increasing":
                return False
            direction = "decreasing"
    
    return True