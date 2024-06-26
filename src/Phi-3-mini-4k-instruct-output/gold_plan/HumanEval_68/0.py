def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [smallest_value, its_index].
    If there are no even values or the given array is empty, return [].

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

    Constraints:
        1 <= nodes.length <= 10000
        0 <= node.value
    """
    if not arr:
        return []

    even_numbers = [num for num in arr if num % 2 == 0]
    if not even_numbers:
        return []

    smallest_even = min(even_numbers)
    index_of_smallest_even = arr.index(smallest_even)

    return [smallest_even, index_of_smallest_even]