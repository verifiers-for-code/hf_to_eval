def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list, [smallest_value, its index].
    If there are no even values or the given array is empty, return [].

    Args:
    arr (list): A list of non-negative integer nodes representing a branch of a tree.

    Returns:
    list: A list containing the smallest even value and its index, or an empty list if no even values are found.

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
    """
    if not arr:
        return []

    smallest_even_value = float('inf')
    smallest_even_index = -1

    for index, value in enumerate(arr):
        if value % 2 == 0:
            if value < smallest_even_value:
                smallest_even_value = value
                smallest_even_index = index

    if smallest_even_value == float('inf'):
        return []

    return [smallest_even_value, smallest_even_index]