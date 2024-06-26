def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1

    Action Plan:
    1. Initialize a variable to store the largest index, set it to -1.
    2. Start a loop from index 1 to the end of the array:
       a. Compare the current element with the previous element.
       b. If the current element is less than the previous element:
          - Update the largest index variable with the current index.
    3. After the loop ends, return the largest index variable.

    Note: This plan ensures we find the largest index satisfying the condition,
    and returns -1 if no such index is found.
    """
    largest_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            largest_index = i
    return largest_index