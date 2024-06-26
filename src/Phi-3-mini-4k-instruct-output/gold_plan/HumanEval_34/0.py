def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Step 1: Convert the input list to a set to remove duplicates
    unique_elements = set(l)

    # Step 2: Convert the set back to a list
    unique_list = list(unique_elements)

    # Step 3: Sort the list in ascending order
    sorted_unique_list = sorted(unique_list)

    # Step 4: Return the sorted list of unique elements
    return sorted_unique_list