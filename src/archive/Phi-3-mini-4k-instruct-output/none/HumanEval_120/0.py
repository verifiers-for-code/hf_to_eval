def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    :param arr: List of integers
    :param k: Positive integer
    :return: List of k maximum integers in arr
    """
    # Check if k is greater than the length of the array
    if k > len(arr):
        return "k is greater than the length of the array"
    
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Return the first k elements
    return arr[:k]