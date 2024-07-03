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
    """
    # Step 1: Create a copy of the input array
    array_copy = array[:]

    # Step 2: Define a helper function to determine the sorting order
    def get_sort_order(array):
        sum_first_last = array[0] + array[-1]
        return 'ascending' if sum_first_last % 2 != 0 else 'descending'

    # Step 3: Implement the main sorting logic
    sort_order = get_sort_order(array_copy)
    if sort_order == 'ascending':
        array_copy.sort()
    else:
        array_copy.sort(reverse=True)

    return array_copy