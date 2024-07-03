def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.

    Args:
    l1 (list): The first list.
    l2 (list): The second list.

    Returns:
    list: A sorted list of unique common elements between l1 and l2.

    Examples:
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    # Step 1: Convert both input lists to sets to remove duplicates and enable efficient set operations
    set1 = set(l1)
    set2 = set(l2)

    # Step 2: Find the common elements between the two sets using the set intersection operation
    common_elements = set1.intersection(set2)

    # Step 3: Convert the resulting set of common elements back to a list
    common_elements_list = list(common_elements)

    # Step 4: Sort the list of common elements in ascending order
    common_elements_list.sort()

    # Step 5: Return the sorted list of common elements
    return common_elements_list