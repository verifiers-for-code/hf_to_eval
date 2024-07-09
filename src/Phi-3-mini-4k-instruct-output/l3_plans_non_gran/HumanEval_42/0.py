def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    

    Action Plan:
    1. Define a function `incr_list` that takes a list `l` as input.
    2. Create a new list `new_list` to store the incremented elements.
    3. Use a mapping function (e.g., `map`) to apply a lambda function to each element in the input list.
        - The lambda function should add 1 to each element.
    4. Convert the resulting map object to a list using the `list` function.
    5. Assign the resulting list to `new_list`.
    6. Return the `new_list` containing the incremented elements."""
    
    new_list = list(map(lambda x: x + 1, l))
    return new_list