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
    1. Check if the input array is empty:
        - If empty, return an empty list
    
    2. Initialize variables to store the smallest even value and its index:
        - Set the smallest even value to infinity
        - Set the index of the smallest even value to -1
    
    3. Iterate through the array:
        - For each element, check if it's even:
            a. If even, compare it with the current smallest even value:
                - If smaller, update the smallest even value and its index
    
    4. After iterating through the array, check if a smallest even value was found:
        - If not, return an empty list
        - If found, return the smallest even value and its index in the specified format: [smallest_value, index]
    
    Note: Use appropriate conditional statements and loops to implement the logic.
    Be careful with indexing and value comparisons.
    """
    if not arr:
        return []

    smallest_even = float('inf')
    smallest_even_index = -1

    for i, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even:
            smallest_even = value
            smallest_even_index = i

    if smallest_even_index == -1:
        return []
    else:
        return [smallest_even, smallest_even_index]