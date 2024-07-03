def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    

    Action Plan:
    1. Understand that the goal is to find unique common elements between two lists and return them in a sorted order.
    2. Convert one or both of the input lists to a set (or a similar data structure) to enable efficient lookups and removal of duplicates.
    3. Iterate through one of the lists and check each element's presence in the other list (or set). If an element is found, add it to a result set.
    4. Convert the result set back to a list and sort it in ascending order.
    5. Return the sorted list of unique common elements."""

    # Convert the lists to sets to remove duplicates and enable efficient lookups
    set1 = set(l1)
    set2 = set(l2)

    # Find the common elements between the two sets
    common_elements = set1.intersection(set2)

    # Convert the set of common elements back to a list and sort it
    sorted_common_elements = sorted(list(common_elements))

    # Return the sorted list of unique common elements
    return sorted_common_elements