def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [smallest_value, its index],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value

    Action Plan:
    1. Check if the input array is empty. If so, return an empty list.
    2. Filter the input array to get a list of even nodes.
    3. Check if the list of even nodes is empty. If so, return an empty list.
    4. Find the smallest even value in the list of even nodes.
    5. Find the index of the smallest even value in the original input array.
    6. Return a list containing the smallest even value and its index in the original array.
    """
    if not arr:
        return []

    even_nodes = [node for node in arr if node % 2 == 0]
    if not even_nodes:
        return []

    smallest_even = min(even_nodes)
    index_of_smallest_even = arr.index(smallest_even)

    return [smallest_even, index_of_smallest_even]