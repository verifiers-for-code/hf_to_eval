def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    

    Action Plan:
    1. Understand that a list is monotonically increasing if each element is greater than or equal to the previous one, and monotonically decreasing if each element is less than or equal to the previous one.
    2. Check if the input list is monotonically increasing by comparing it to a sorted version of itself.
    3. Check if the input list is monotonically decreasing by comparing it to a sorted version of itself in reverse order.
    4. Implement the monotonic function to return True if the list satisfies either of the above conditions, and False otherwise."""

    # Check if the list is monotonically increasing
    if l == sorted(l):
        return True

    # Check if the list is monotonically decreasing
    if l == sorted(l, reverse=True):
        return True

    # If neither condition is met, return False
    return False