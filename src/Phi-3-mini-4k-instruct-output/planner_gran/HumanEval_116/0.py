def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    

    1. Define the function signature:
       - The function takes a list of non-negative integers as input
       - The function returns a sorted list of integers
    
    2. Create a helper function to count the number of ones in a binary representation:
       - This function will take an integer as input
       - It will return the number of ones in the binary representation of the input integer
       - Use bitwise operations to count the number of ones (e.g., count = 0, while n: n &= (n - 1); count += n)
    
    3. Implement the sorting algorithm:
       - Use a suitable sorting algorithm (e.g., selection sort, bubble sort, or insertion sort)
       - The sorting algorithm should sort the input list based on the number of ones in the binary representation
       - If the number of ones is the same, sort based on the decimal value
    
    4. Handle the sorting criteria:
       - In the sorting algorithm, use the helper function to count the number of ones in the binary representation
       - Compare the number of ones and the decimal value to determine the sorting order
       - Ensure that the sorting algorithm is stable to maintain the original order of elements with the same number of ones
    
    5. Test the function with various input examples:
       - Use the provided unit tests to verify the correctness of the implementation
       - Test edge cases, such as empty input lists, lists with a single element, and lists with multiple elements
    
    Additional implementation details:
    - Consider using a lambda function or a separate function for the sorting key
    - Ensure the sorting algorithm is efficient and scalable for large input lists
    - Handle potential errors and edge cases, such as invalid input types or values"""

    def count_ones(n):
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count

    def sort_key(x):
        return (count_ones(x), x)

    return sorted(arr, key=sort_key)