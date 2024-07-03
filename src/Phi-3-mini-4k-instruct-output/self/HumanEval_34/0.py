def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Step 1: Sort the list
    l.sort()

    # Step 2: Extract unique elements
    unique_elements = []
    for element in l:
        if element not in unique_elements:
            unique_elements.append(element)

    # Step 3: Sort the extracted unique elements
    unique_elements.sort()

    return unique_elements