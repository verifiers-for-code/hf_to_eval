def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    # Step 1: Convert lists to sets
    set1 = set(l1)
    set2 = set(l2)
    
    # Step 2: Perform intersection to find common elements
    common_elements = set1.intersection(set2)
    
    # Step 3: Convert intersection set to a list
    common_elements_list = list(common_elements)
    
    # Step 4: Sort the list of common elements
    common_elements_list.sort()
    
    # Step 5: Return the sorted list of common elements
    return common_elements_list