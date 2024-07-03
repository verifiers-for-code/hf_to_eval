def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    

    Action Plan:
    1. Sort the input list in ascending order.
    2. Determine if the length of the sorted list is odd or even.
    3. If the length is odd:
       a. Return the middle element of the sorted list (at index length // 2).
    4. If the length is even:
       a. Calculate the average of the two middle elements (at indices length // 2 - 1 and length // 2).
       b. Return this average value as the median.
    5. Return the calculated median value."""
    
    l.sort()
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]