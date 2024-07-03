def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    

    Action Plan:
    1. Initialize a variable to store the largest index of the desired element, initially set to -1.
    2. Iterate through the input array, starting from the second element (index 1):
       a. Compare the current element with the previous element.
       b. If the current element is less than the previous element, update the result index to the current index.
    3. Continue iterating through the array until the end.
    4. Return the final result index, which is the largest index of an element that is not greater than or equal to the element immediately preceding it. If no such element exists, return -1."""
    
    result_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            result_index = i
    return result_index