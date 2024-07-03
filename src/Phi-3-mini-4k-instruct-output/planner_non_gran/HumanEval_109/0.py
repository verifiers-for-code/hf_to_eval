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
    1. Check if the input array is empty:
        - If true, return True (an empty array is already sorted)
    
    2. Calculate the number of right shifts needed to sort the array:
        - Find the maximum element in the array
        - Calculate the number of right shifts by subtracting the index of the maximum element from the length of the array
    
    3. Check if the number of right shifts is possible:
        - If the number of right shifts is greater than the length of the array, return False (not possible to sort the array)
    
    4. Return True if the number of right shifts is possible, False otherwise
    
    Note: Use appropriate array methods for finding the maximum element and calculating the number of right shifts.
    Be careful with the edge case of an empty array."""

    # Check if the input array is empty
    if not arr:
        return True

    # Find the maximum element in the array
    max_element = max(arr)

    # Calculate the number of right shifts needed to sort the array
    num_right_shifts = len(arr) - arr.index(max_element)

    # Check if the number of right shifts is possible
    if num_right_shifts > len(arr):
        return False

    return True