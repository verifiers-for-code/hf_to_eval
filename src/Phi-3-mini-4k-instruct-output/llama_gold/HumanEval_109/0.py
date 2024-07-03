def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    

    Action Plan:
    1. Check if the input array is empty. If so, return True.
    2. Find the minimum value in the array and its index.
    3. Rotate the array to the right by the minimum index, effectively moving the minimum value to the start of the array.
    4. Create a sorted copy of the original array.
    5. Compare the rotated array with the sorted array element-wise.
       a. If all elements match, return True, indicating that the array can be sorted by right shifting.
       b. If any elements don't match, return False, indicating that the array cannot be sorted by right shifting."""

    # Check if the input array is empty
    if not arr:
        return True

    # Find the minimum value and its index
    min_val = min(arr)
    min_index = arr.index(min_val)

    # Rotate the array to the right by the minimum index
    rotated_arr = arr[min_index:] + arr[:min_index]

    # Create a sorted copy of the original array
    sorted_arr = sorted(arr)

    # Compare the rotated array with the sorted array element-wise
    for i in range(len(arr)):
        if rotated_arr[i] != sorted_arr[i]:
            return False

    return True