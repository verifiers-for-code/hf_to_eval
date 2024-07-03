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
    1. Initialize a variable to store the minimum number of changes required, set it to 0.
    2. Iterate through the array from the start to the middle (inclusive).
    3. For each element, check if it is not equal to its corresponding element from the end of the array (i.e., arr[i]!= arr[-i-1]).
    4. If the elements are not equal, increment the minimum number of changes by 1.
    5. After the iteration, return the minimum number of changes required.
    
    Note: The iteration stops at the middle of the array because changing elements beyond the middle would not affect the palindromic property."""
    
    min_changes = 0
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            min_changes += 1
    return min_changes