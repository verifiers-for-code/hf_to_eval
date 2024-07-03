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
    1. Define a helper function to perform a right shift operation on an array and return the result:
        - Move the last element to the first position
    
    2. Define a helper function to check if the given array can be sorted with the right shift operation:
        a. Generate the sorted version of the input array using sorting
        b. Apply the right shift operation repeatedly until the original array equals the sorted sorted array
        c. If the final array equals the sorted array, return True
        d. Otherwise, return False
    
    3. Consider edge cases:
        a. Empty array (return True)
        b. Array with one element (return True)
        c. Already sorted array (return True)
    
    4. Evaluate the initial array state to determine the feasibility of sorting:
        a. If the first element is greater than the last element, sorting is not possible with the operation (return False)
        b. Otherwise, attempt to sort the array by shifting and compare with the sorted array
    
    5. Account for efficiency by minimizing array comparisons and implementing efficient shift operations
    
    6. Test the solution with provided examples and potential edge cases to ensure correctness"""

    def right_shift(arr):
        """Perform a right shift operation on the array and return the result."""
        return [arr[-1]] + arr[:-1]

    def can_sort_with_shifts(arr):
        """Check if the array can be sorted with right shift operations."""
        sorted_arr = sorted(arr)
        while arr != sorted_arr:
            arr = right_shift(arr)
        return arr == sorted_arr

    # Edge cases
    if not arr:
        return True
    if len(arr) == 1:
        return True
    if arr == sorted(arr):
        return True

    # Evaluate initial array state
    if arr[0] > arr[-1]:
        return False

    return can_sort_with_shifts(arr)