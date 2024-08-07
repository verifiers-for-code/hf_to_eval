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
    2. If the array is not empty:
       a. Calculate the sum of the first and last elements of the array.
       b. Determine if this sum is odd or even.
    3. Create a copy of the input array to avoid modifying the original.
    4. Sort the copy of the array:
       - If the sum is odd, sort in ascending order.
       - If the sum is even, sort in descending order.
    5. Return the sorted copy of the array.
    """
    if not array:
        return []

    first_element = array[0]
    last_element = array[-1]
    sum_first_last = first_element + last_element

    sorted_array = array.copy()

    if sum_first_last % 2 == 0:
        sorted_array.sort(reverse=True)
    else:
        sorted_array.sort()

    return sorted_array