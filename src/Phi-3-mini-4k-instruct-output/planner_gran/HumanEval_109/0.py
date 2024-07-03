def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N]. The numbers in the array will be randomly ordered. Your task is to determine if it is possible to get an array sorted in non-decreasing order by performing the following operation on the given array:
    You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one position in the right direction. The last element of the array will be moved to the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:

    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performing 2 right shift operations, non-decreasing order can be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation: It is not possible to get non-decreasing order for the given array by performing any number of right shift operations.

    1. Check if the input array is empty:
       - If the array is empty, return True (since an empty array is considered sorted)

    2. Check if the input array is already sorted:
       - Compare the input array with its sorted version
       - If they are equal, return True (since the array is already sorted)

    3. Initialize a variable to track the number of right shift operations:
       - Initialize a variable (e.g., 'shifts') to 0

    4. Perform right shift operations:
       - While the array is not sorted, perform a right shift operation
       - Increment the 'shifts' variable by 1
       - Shift all elements of the array to the right by 1 position
       - Update the array with the shifted values

    5. Check if the array is sorted after each operation:
       - Compare the current array with its sorted version
       - If they are equal, break the loop (since the array is sorted)

    6. Return the result:
       - If the array is sorted, return True
       - Otherwise, return False

    Additional implementation details:
    - Use the appropriate array methods for sorting and shifting elements
    - Ensure that the function handles edge cases, such as an array with a single element
    - Consider using a more efficient sorting algorithm if the input array is very large"""

    if not arr:
        return True

    if arr == sorted(arr):
        return True

    shifts = 0
    while arr != sorted(arr):
        arr = [arr[-1]] + arr[:-1]
        shifts += 1

    return shifts > 0