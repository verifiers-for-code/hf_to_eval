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
    1. Create a copy of the input array to avoid modifying the original array.
    2. Calculate the sum of the first and last elements of the copied array.
    3. Determine the sorting order based on the sum:
        - If the sum is odd, sort the array in ascending order
        - If the sum is even, sort the array in descending order
    4. Use the appropriate sorting method (e.g., `sorted()` or `list.sort()`) to sort the array in the determined order.
    5. Return the sorted array.

    Note: Be careful when copying the array to avoid modifying the original input.
    Consider using a conditional statement to determine the sorting order based on the sum.
    """
    # Step 1: Create a copy of the input array
    sorted_array = array.copy()

    # Step 2: Calculate the sum of the first and last elements
    sum_first_last = sorted_array[0] + sorted_array[-1]

    # Step 3: Determine the sorting order based on the sum
    if sum_first_last % 2 == 0:
        # If the sum is even, sort the array in descending order
        sorted_array.sort(reverse=True)
    else:
        # If the sum is odd, sort the array in ascending order
        sorted_array.sort()

    # Step 5: Return the sorted array
    return sorted_array