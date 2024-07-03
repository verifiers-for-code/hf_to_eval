def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)

    Action Plan:
    1. Handle the edge case:
       - Check if k is 0. If so, return an empty list.

    2. Sort the input array:
       - Use a built-in sorting method to sort the entire array in ascending order.

    3. Select the maximum k elements:
       - Create a new list containing the last k elements of the sorted array.
       - These will be the k largest elements in ascending order.

    4. Return the result:
       - Return the list created in step 3.

    Note: This approach sorts the entire array, which is efficient for most cases.
    For very large arrays with small k, other approaches might be more optimal.
    """
    if k == 0:
        return []

    arr.sort()
    return arr[-k:]