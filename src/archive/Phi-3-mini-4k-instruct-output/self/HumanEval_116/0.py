def sort_array(arr):
    """
    Sorts an array of non-negative integers based on the number of ones in their binary representation in ascending order.
    For similar number of ones, sorts based on decimal value.

    :param arr: List of non-negative integers
    :return: Sorted list of integers
    """
    # Step 1: Prepare the array for sorting
    arr_with_bin = [(num, bin(num).count('1')) for num in arr]

    # Step 2: Sort the list using a custom key
    arr_sorted = sorted(arr_with_bin, key=lambda x: (x[1], x[0]))

    # Extracting the sorted numbers from the tuples
    sorted_arr = [num for num, _ in arr_sorted]

    return sorted_arr