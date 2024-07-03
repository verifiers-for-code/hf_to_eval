def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    

    Action Plan:
    1. Convert both input lists `l1` and `l2` to sets to remove duplicates and enable efficient set operations.
    2. Find the common elements between the two sets using the set intersection operation.
    3. Convert the resulting set of common elements back to a list.
    4. Sort the list of common elements in ascending order.
    5. Return the sorted list of common elements.
    
    Note: Use the built-in `set` data structure and its `intersection` method to find the common elements.
    Be careful when converting between lists and sets, as this can affect the order of elements."""
    set1 = set(l1)
    set2 = set(l2)
    common_elements = list(set1.intersection(set2))
    common_elements.sort()
    return common_elements