def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True

    Action Plan:
    1. Understand that a monotonic list can be either increasing or decreasing
    2. Create a sorted version of the input list in ascending order
    3. Create another sorted version of the input list in descending order
    4. Compare the original list with both sorted versions
    5. If the original list matches either of the sorted versions, it is monotonic
    6. Return True if the list is monotonic, False otherwise

    Hints:
    - Use the sorted() function to create sorted versions of the list
    - For descending order, use the reverse parameter in sorted()
    - Use comparison (==) to check if lists are equal
    - Combine the comparisons using the OR (or) operator
    """
    ascending = sorted(l)
    descending = sorted(l, reverse=True)
    return l == ascending or l == descending