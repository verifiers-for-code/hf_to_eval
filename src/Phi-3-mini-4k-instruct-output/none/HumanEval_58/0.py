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
    # Convert lists to sets to remove duplicates and find common elements
    set1, set2 = set(l1), set(l2)
    common_elements = sorted(list(set1 & set2))
    return common_elements