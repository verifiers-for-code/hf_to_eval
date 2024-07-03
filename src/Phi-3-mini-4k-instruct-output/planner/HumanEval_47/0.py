def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    

    Action Plan:
    1. Sort the input list in ascending order using a suitable sorting algorithm or built-in function.
    2. Determine the length of the sorted list.
    3. Check if the length of the list is even or odd:
        a. If even:
            - Calculate the median as the average of the two middle elements.
        b. If odd:
            - Calculate the median as the middle element.
    4. Return the calculated median value.
    
    Note: Consider using a built-in function for sorting to simplify the implementation.
    Be careful when handling even and odd-length lists to avoid errors."""
    
    # Step 1: Sort the input list in ascending order
    l.sort()
    
    # Step 2: Determine the length of the sorted list
    n = len(l)
    
    # Step 3: Check if the length of the list is even or odd
    if n % 2 == 0:
        # If even, calculate the median as the average of the two middle elements
        median_value = (l[n//2 - 1] + l[n//2]) / 2
    else:
        # If odd, calculate the median as the middle element
        median_value = l[n//2]
    
    # Step 4: Return the calculated median value
    return median_value