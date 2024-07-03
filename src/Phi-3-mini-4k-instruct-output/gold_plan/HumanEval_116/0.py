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
    1. Define a helper function to count the number of '1's in the binary representation of a number:
       a. Convert the number to its binary representation (hint: use a built-in function).
       b. Remove the '0b' prefix from the binary string.
       c. Count the occurrences of '1' in the resulting string.

    2. Use the sorted() function twice:
       a. First, sort the input array based on the decimal values (inner sorted()).
       b. Then, sort the result based on the count of '1's in binary representation (outer sorted()).

    3. For the outer sorted() function, use a key parameter:
       a. The key should be a lambda function that calls the helper function from step 1.

    4. Return the final sorted array.

    Note: This approach ensures that for equal number of '1's in binary representation,
    the sorting is based on decimal value due to the stable nature of Python's sorting algorithm.
    """

    # Helper function to count the number of '1's in the binary representation of a number
    def count_ones(n):
        binary_str = bin(n)[2:]  # Convert to binary and remove '0b' prefix
        return binary_str.count('1')

    # Sort the array based on the decimal values (inner sorted())
    arr = sorted(arr)

    # Sort the result based on the count of '1's in binary representation (outer sorted())
    arr = sorted(arr, key=lambda x: (count_ones(x), x))

    return arr