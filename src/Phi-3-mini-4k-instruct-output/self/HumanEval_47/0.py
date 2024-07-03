def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    

    Action Plan:
    1. Handle an empty list by returning None or an appropriate value
    
    2. Calculate the median's location:
        a. If the length is odd, the median is at index (length - 1) / 2
        b. If the length is even, the median is at (length / 2) - 1 and (length / 2)
    
    3. Sort the list if not already sorted, or apply an efficient algorithm for median-finding
        - For small lists (<= 10 elements), sorting and picking middle elements are efficient
        - For larger lists, consider quickselect or a linear time median-finding algorithm
    
    4. Ensure handling of repeated values:
        - In the sorted case, if there are repeated values, take the average of the two middle values for an even-length list
        - Otherwise, the duplicate values should not affect the median calculation
    
    5. Return the median or the appropriate median value
    
    6. Test the function with various test cases, including empty lists, lists with an odd number of elements, and lists with an even number of elements"""

    if not l:
        return None

    l.sort()

    n = len(l)
    mid = n // 2

    if n % 2 == 0:
        return (l[mid - 1] + l[mid]) / 2
    else:
        return l[mid]