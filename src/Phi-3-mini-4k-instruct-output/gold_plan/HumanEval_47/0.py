def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Step 1: Sort the input list in ascending order
    l.sort()

    # Step 2: Determine the length of the sorted list
    n = len(l)

    # Step 3: Check if the length is odd or even
    if n % 2 == 0:
        # If even:
        # Calculate the indices of the two middle elements
        mid1 = n // 2 - 1
        mid2 = n // 2

        # Compute the average of the two middle elements
        median_value = (l[mid1] + l[mid2]) / 2.0
    else:
        # If odd:
        # Calculate the index of the middle element using integer division
        mid = n // 2

        # Return the element at that index
        median_value = l[mid]

    return median_value