def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    

    Action Plan:
    1. Check if the input array is empty. If so, return an empty array.
    2. Calculate the sum of the first and last elements of the array.
    3. Determine the sorting order:
       a. If the sum is odd, sort the array in ascending order.
       b. If the sum is even, sort the array in descending order.
    4. Create a copy of the input array to avoid modifying the original.
    5. Sort the copied array according to the determined order.
    6. Return the sorted array."""

    # Step 1: Check if the input array is empty
    if not array:
        return []

    # Step 2: Calculate the sum of the first and last elements
    sum_first_last = array[0] + array[-1]

    # Step 3: Determine the sorting order
    if sum_first_last % 2 == 0:
        # Sort in descending order
        sorted_array = sorted(array, reverse=True)
    else:
        # Sort in ascending order
        sorted_array = sorted(array)

    # Step 4: Create a copy of the input array
    sorted_array_copy = sorted_array.copy()

    # Step 5: Return the sorted array
    return sorted_array_copy