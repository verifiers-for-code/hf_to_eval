def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0

    Action Plan:
    1. Sort the input list in ascending order.
    2. Determine the length of the sorted list.
    3. Check if the length is odd or even:
       a. If odd:
          - Calculate the index of the middle element using integer division.
          - Return the element at that index.
       b. If even:
          - Calculate the indices of the two middle elements.
          - Compute the average of the two middle elements.
          - Return the result as a float.

    Note: Remember to handle integer division correctly and ensure
    the result is a float for even-length lists.
    """
    l.sort()
    n = len(l)
    if n % 2 == 0:
        mid1 = l[n//2 - 1]
        mid2 = l[n//2]
        return (mid1 + mid2) / 2.0
    else:
        return l[n//2]