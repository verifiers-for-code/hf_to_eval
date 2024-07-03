def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    

    Action Plan:
    1. Define a function `unique` that takes a list `l` as input.
    2. Convert the input list `l` to a set using the `set()` function to remove duplicates.
    3. Convert the set back to a list using the `list()` function.
    4. Sort the list in ascending order using the `sorted()` function.
    5. Return the sorted list of unique elements.
    
    Note: The `set()` function automatically removes duplicates, and the `sorted()` function sorts the list in ascending order.
    Be careful to convert the set back to a list before sorting, as the `sorted()` function only works with lists."""
    return sorted(list(set(l)))