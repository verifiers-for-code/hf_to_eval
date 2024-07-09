def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    

    Action Plan:
    1. Define the function `common` with two parameters: `l1` and `l2`, both lists.
    2. Convert `l1` and `l2` into sets to remove duplicates and enable efficient set operations.
    3. Use the `intersection` method to find the common elements between the two sets.
    4. Convert the resulting set back into a list.
    5. Sort the list of common elements in ascending order.
    6. Return the sorted list of common elements.
    
    Note: Use the `set` data structure to remove duplicates and enable efficient operations.
    Use the `intersection` method to find the common elements between the two sets.
    Sort the result in ascending order to ensure consistency."""
    set1 = set(l1)
    set2 = set(l2)
    common_elements = list(set1.intersection(set2))
    common_elements.sort()
    return common_elements