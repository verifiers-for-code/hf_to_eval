def median(l: list):
    """Return median of elements in the list l.

    Args:
    l (list): A list of numbers.

    Returns:
    float: The median of the elements in the list.

    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    10.0
    """
    # Sort the list
    l.sort()

    # Calculate the length of the list
    n = len(l)

    # Check if the list has an even number of elements
    if n % 2 == 0:
        # If even, return the average of the two middle elements
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        # If odd, return the middle element
        return l[n//2]