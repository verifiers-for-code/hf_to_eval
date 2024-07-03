def get_positive(l: list):
    """Return only positive numbers in the list.

    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # Step 1: Create a list comprehension to filter the input list
    positive_numbers = [num for num in l if num > 0]

    # Step 2: Consider zero as a positive number if desired
    # positive_numbers = [num for num in l if num >= 0]

    # Step 3: Handle edge cases
    if not l:  # An empty list
        return []

    # The list comprehension already handles various number ranges and types (integers and floats)

    return positive_numbers