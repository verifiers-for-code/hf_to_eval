def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    

    Action Plan:
    1. Define a function `monotonic` that takes a list `l` as input.
    2. Initialize a variable to store the result, which will be a boolean value.
    3. Iterate through the list `l` starting from the second element (index 1):
        a. For each element, compare it with the previous element.
        b. Check if the current element is less than or equal to the previous element (for increasing order) or greater than or equal to the previous element (for decreasing order).
        c. If the comparison fails (i.e., the current element is not in the correct order), set the result to `False` and break the loop.
    4. If the loop completes without finding any violating elements, set the result to `True`.
    5. Return the result.
    6. Consider edge cases, such as an empty list or a list with a single element, and handle them accordingly.
    
    Note: Use a simple and efficient algorithm to check for monotonicity. Be careful with indexing and comparison logic."""
    if len(l) < 2:
        return True
    increasing = l[1] > l[0]
    for i in range(2, len(l)):
        if (increasing and l[i] <= l[i-1]) or (not increasing and l[i] >= l[i-1]):
            return False
    return True