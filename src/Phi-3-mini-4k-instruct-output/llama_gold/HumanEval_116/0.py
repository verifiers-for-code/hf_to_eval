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
    1. Ensure the input array only contains non-negative integers.
    2. Prepare a sorting key function that calculates the number of ones in the binary representation of each integer.
    3. Use a sorting algorithm that first sorts the array based on the decimal value of the integers.
    4. Then, use the prepared sorting key function to sort the array based on the number of ones in the binary representation.
    5. Return the sorted array.
    
    Note: Consider using a stable sorting algorithm to maintain the order of elements with the same number of ones in their binary representation."""

    # Step 1: Ensure the input array only contains non-negative integers.
    if not all(isinstance(x, int) and x >= 0 for x in arr):
        raise ValueError("Input array must only contain non-negative integers.")

    # Step 2: Prepare a sorting key function that calculates the number of ones in the binary representation of each integer.
    def count_ones(n):
        return bin(n).count('1')

    # Step 3: Use a sorting algorithm that first sorts the array based on the decimal value of the integers.
    arr.sort()

    # Step 4: Then, use the prepared sorting key function to sort the array based on the number of ones in the binary representation.
    arr.sort(key=count_ones)

    # Step 5: Return the sorted array.
    return arr