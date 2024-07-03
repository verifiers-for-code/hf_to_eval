def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    

    Action Plan:
    1. Initialize a counter to store the minimum number of changes needed.
    2. Iterate through the first half of the input array:
       a. For each element, compare it with the corresponding element from the end of the array (mirrored index).
       b. If the elements don't match, increment the change counter.
    3. Return the change counter, which represents the minimum number of elements that need to be changed to make the array palindromic.
    """
    n = len(arr)
    changes = 0
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            changes += 1
    return changes