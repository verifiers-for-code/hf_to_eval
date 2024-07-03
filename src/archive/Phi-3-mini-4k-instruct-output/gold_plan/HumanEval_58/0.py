def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.

    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    # Step 1: Initialize an empty container to store common elements.
    common_elements = set()

    # Step 2: Iterate through each element in the first list (l1).
    for element in l1:
        # Step 3: For each element in l1, check if it exists in the second list (l2).
        if element in l2:
            # Step 4: If an element is found in both lists, add it to the container.
            common_elements.add(element)

    # Step 5: Convert the container to a list of unique elements.
    common_elements = list(common_elements)

    # Step 6: Sort the list of common elements in ascending order.
    common_elements.sort()

    # Step 7: Return the sorted list of common elements.
    return common_elements