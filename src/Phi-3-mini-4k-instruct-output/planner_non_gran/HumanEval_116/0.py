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
    1. Understand the sorting criteria:
        - Sort the array based on the number of ones in the binary representation of each element
        - If two elements have the same number of ones, sort them based on their decimal value
    
    2. Create a custom sorting function:
        - Define a function `sort_array` that takes an array `arr` as input
        - Use the `sorted` function with a custom sorting key
    
    3. Implement the sorting logic:
        - Define a lambda function `sort_key` as the sorting key
        - In `sort_key`, convert each element to its binary representation using `bin`
        - Count the number of ones in the binary representation using `count('1')`
        - Return a tuple with the count of ones and the decimal value of the element
    
    4. Handle edge cases:
        - Consider negative numbers in the input array
        - Ensure the sorting logic works correctly for all input values
    
    5. Return the sorted array:
        - Use the `sorted` function with the custom sorting key to sort the input array
        - Return the sorted array
    
    Note: Use the `bin` function to convert integers to binary strings, and the `count` method to count the number of ones in the binary representation."""
    
    # Define the custom sorting key
    sort_key = lambda x: (bin(x).count('1'), x)
    
    # Sort the array using the custom sorting key
    sorted_arr = sorted(arr, key=sort_key)
    
    # Return the sorted array
    return sorted_arr