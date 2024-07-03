def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    Action Plan:
    1. Initialize an empty container to store common elements.
    2. Iterate through each element in the first list (l1).
    3. For each element in l1, check if it exists in the second list (l2).
    4. If an element is found in both lists, add it to the container.
    5. Convert the container to a list of unique elements.
    6. Sort the list of common elements in ascending order.
    7. Return the sorted list of common elements.

    Note: Consider using an efficient data structure to store and remove duplicates.
    """
    common_elements = set()
    for element in l1:
        if element in l2:
            common_elements.add(element)
    return sorted(list(common_elements))