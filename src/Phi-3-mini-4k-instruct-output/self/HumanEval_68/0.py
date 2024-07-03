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
    1. Initialize variables:
        a. Set a variable `smallest_even` to None
        b. Set `smallest_even_index` to None
    
    2. Loop through the given array with indices:
        a. Check if the current node's value is even.
        b. If it is, compare it to `smallest_even`:
            i. If it's smaller, or the `smallest_even` is None (indicating no even numbers have been found yet):
                - Update `smallest_even` and `smallest_even_index` with the current node's value and index.
    
    3. After the loop, if `smallest_even` remains None, return an empty list as no even values exist.
    
    4. Otherwise, return a list `[smallest_even, smallest_even_index]` as the result.
    """
    smallest_even = None
    smallest_even_index = None

    for index, value in enumerate(arr):
        if value % 2 == 0:
            if smallest_even is None or value < smallest_even:
                smallest_even = value
                smallest_even_index = index

    if smallest_even is None:
        return []
    else:
        return [smallest_even, smallest_even_index]