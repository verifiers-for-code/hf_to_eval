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
    1. Define the function smallest_change that takes an array arr as input.
    2. Initialize two variables: min_changes to store the minimum number of changes, and reversed_arr to store the reversed array.
    3. Iterate through the array using a nested loop:
        a. Iterate through each element in the array.
        b. For each element, iterate through the remaining elements in the array.
        c. Compare the current element with the corresponding element from the end of the array.
        d. If they are not equal, swap them.
        e. Check if the current array is palindromic by comparing it with its reverse.
        f. If it's palindromic, update min_changes with the minimum number of changes so far.
    4. After the iteration, return min_changes as the minimum number of changes required to make the array palindromic.
    5. Consider the time complexity of the solution and optimize it if possible.
    
    Note: Be careful with the indexing and swapping elements in the array.
    Make sure to update the minimum number of changes correctly.
    """
    min_changes = len(arr)
    reversed_arr = arr[::-1]

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] != reversed_arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                if arr == reversed_arr:
                    min_changes = min(min_changes, j - i + 1)
                arr[i], arr[j] = arr[j], arr[i]

    return min_changes