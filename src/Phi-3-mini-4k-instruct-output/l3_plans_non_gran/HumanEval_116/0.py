def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    

    Action Plan:
    1. Define a function `sort_array` that takes an array of non-negative integers as input.
    2. Initialize an empty list to store the sorted array.
    3. Iterate through each number in the input array:
        a. Convert the number to its binary representation using the `bin` function.
        b. Count the number of ones in the binary representation using the `count` method.
        c. Append a tuple containing the count of ones and the decimal value of the number to the list.
    4. Sort the list of tuples based on the count of ones and decimal value in ascending order.
    5. Extract the sorted numbers from the list of tuples and store them in the sorted array.
    6. Return the sorted array.
    
    Note: Be careful when handling edge cases, such as an empty input array or an array with only one element.
    Use the `sorted` function with a custom key function to sort the array."""
    if not arr:
        return []
    if len(arr) == 1:
        return arr
    sorted_arr = sorted(arr, key=lambda x: (bin(x).count('1'), x))
    return sorted_arr