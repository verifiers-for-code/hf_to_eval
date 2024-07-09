def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    

    Action Plan:
    1. Take the input list `l` as a parameter.
    2. Sort the list in ascending order using an appropriate sorting method.
    3. Determine the length of the sorted list using the `len()` function.
    4. Calculate the median based on the list length:
        a. If the length is odd:
            - Return the middle element of the sorted list.
        b. If the length is even:
            - Calculate the two middle elements of the sorted list.
            - Return the average of these two middle elements.
    5. Consider edge cases:
        - Handle empty lists or lists with a single element.
        - Ensure the function works correctly for lists with both odd and even lengths.
    6. Return the calculated median value.
    
    Note: Use appropriate list methods for sorting and indexing.
    Be careful with the calculation for even-length lists to avoid errors."""
    
    # Step 1: Take the input list `l` as a parameter.
    l.sort()
    
    # Step 2: Determine the length of the sorted list using the `len()` function.
    n = len(l)
    
    # Step 3: Calculate the median based on the list length.
    if n % 2 == 0:
        # If the length is even, calculate the two middle elements of the sorted list.
        # Return the average of these two middle elements.
        median_value = (l[n//2 - 1] + l[n//2]) / 2
    else:
        # If the length is odd, return the middle element of the sorted list.
        median_value = l[n//2]
    
    # Step 5: Consider edge cases.
    # Handle empty lists or lists with a single element.
    if n == 0:
        return None
    elif n == 1:
        return l[0]
    
    # Step 6: Return the calculated median value.
    return median_value