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
    1. Initialize a variable to store the number of right shifts required.
    2. Sort the input array in non-decreasing order.
    3. Iterate through the sorted array:
        a. For each element, compare it with the next element.
        b. If the current element is greater than the next element, increment the right shift count.
    4. Check if the number of right shifts required is valid:
        a. If the number of right shifts is less than or equal to the length of the array minus the index of the current element, return True.
        b. Otherwise, return False.
    5. Handle edge cases:
        a. If the input array is empty, return True.
        b. If the input array has only one element, return True.
    
    Note: Use a sorting algorithm to sort the array efficiently.
    Be careful when counting the number of right shifts required.
    Consider edge cases and handle them accordingly."""
    
    if not arr:
        return True
    
    sorted_arr = sorted(arr)
    right_shifts = 0
    
    for i in range(len(arr)):
        if arr[i] > sorted_arr[i]:
            right_shifts += 1
    
    return right_shifts <= len(arr) - i