def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list, [smallest_value, its index].
    If there are no even values or the given array is empty, return [].

    Args:
        arr (List[int]): The input array representing a branch of a tree.

    Returns:
        List[int]: A list containing the smallest even value and its index, or an empty list if no even values are found.
    """
    even_values = [x for x in arr if x % 2 == 0]
    if not even_values:
        return []

    smallest_even_value = min(even_values)
    smallest_even_index = arr.index(smallest_even_value)

    return [smallest_even_value, smallest_even_index]