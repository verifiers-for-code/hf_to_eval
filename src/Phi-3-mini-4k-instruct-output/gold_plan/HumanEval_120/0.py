def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    :param arr: List of integers
    :param k: Positive integer
    :return: List of k maximum numbers in arr
    """
    # Step 1: Handle the edge case
    if k == 0:
        return []

    # Step 2: Sort the input array
    arr.sort()

    # Step 3: Select the maximum k elements
    result = arr[-k:]

    # Step 4: Return the result
    return result