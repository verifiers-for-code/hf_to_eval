from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3.0
    >>> median([-10, 4, 6, 1000, 10, 20])
    12.0
    """
    # Step 1: Handle an empty list
    if not l:
        return None

    # Step 2: Calculate the median's location
    n = len(l)
    mid = n // 2

    # Step 3: Sort the list
    l.sort()

    # Step 4: Handle repeated values
    if n % 2 == 0:
        return (l[mid - 1] + l[mid]) / 2.0
    else:
        return l[mid]