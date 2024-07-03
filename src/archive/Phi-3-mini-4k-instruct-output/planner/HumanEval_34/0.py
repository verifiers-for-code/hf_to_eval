def unique(l: list) -> list:
    """Return sorted unique elements in a list

    Args:
    l (list): A list of elements

    Returns:
    list: A sorted list of unique elements

    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]

    Action Plan:
    1. Define a function `unique` that takes a list `l` as input.
    2. Convert the input list `l` to a set using the `set()` function to remove duplicates.
    3. Convert the set back to a list using the `list()` function.
    4. Sort the list in ascending order using the `sorted()` function.
    5. Return the sorted list of unique elements.
    """
    unique_elements = list(set(l))
    sorted_unique_elements = sorted(unique_elements)
    return sorted_unique_elements