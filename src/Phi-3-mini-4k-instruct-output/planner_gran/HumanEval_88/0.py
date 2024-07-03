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
    

    1. Handle edge cases:
       - Check if the input array is empty or has only one element
       - If true, return the original array (no sorting needed)
    
    2. Calculate the sum of the first and last elements:
       - Use indexing to access the first and last elements of the array
       - Add these elements together to get the sum
    
    3. Determine the sorting order:
       - Check if the sum is odd or even
       - If odd, sort the array in ascending order
       - If even, sort the array in descending order
    
    4. Create a copy of the array and sort it:
       - Use the appropriate sorting method (e.g., sorted() or list.sort())
       - Pass the sorting order (ascending or descending) as an argument
    
    5. Return the sorted array:
       - Return the sorted copy of the original array
    
    Additional implementation details:
    - Use the appropriate array methods for indexing, copying, and sorting
    - Consider using the modulo operator (%) to check if the sum is odd or even
    - Ensure that the function handles arrays with a single element correctly
    - Test the function with various input arrays to verify its correctness"""

    if len(array) == 0:
        return array
    elif len(array) == 1:
        return array

    first_element = array[0]
    last_element = array[-1]
    sum_first_last = first_element + last_element

    if sum_first_last % 2 == 0:
        sorted_array = sorted(array, reverse=True)
    else:
        sorted_array = sorted(array)

    return sorted_array