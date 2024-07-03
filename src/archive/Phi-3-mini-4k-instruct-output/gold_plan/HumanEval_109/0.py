def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].
    The numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.

    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index.

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Action Plan:
    1. Check if the input array is empty. If so, return True.
    2. Create a sorted version of the input array for later comparison.
    3. Find the minimum value in the input array.
    4. Find the index of the minimum value.
    5. Reconstruct the array by concatenating:
       a. Elements from the minimum value to the end of the array
       b. Elements from the start of the array to the minimum value (exclusive)
    6. Compare the reconstructed array with the sorted array:
       a. Iterate through both arrays simultaneously
       b. If any elements don't match, return False
    7. If all elements match, return True
    """
    if not arr:
        return True

    sorted_arr = sorted(arr)
    min_val = min(arr)
    min_index = arr.index(min_val)

    reconstructed_arr = arr[min_index:] + arr[:min_index]

    for i in range(len(reconstructed_arr)):
        if reconstructed_arr[i] != sorted_arr[i]:
            return False

    return True