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
    1. Understand the problem requirements:
        - The function takes an array of non-negative integers as input
        - The function should return a copy of the input array after sorting
        - The sorting order is determined by the sum of the first and last elements of the array
    
    2. Create a copy of the input array:
        - Use the copy() method to create a shallow copy of the input array
        - This ensures the original array remains unchanged
    
    3. Calculate the sum of the first and last elements:
        - Access the first and last elements of the array using indexing (array[0] and array[-1])
        - Calculate the sum of these two elements
    
    4. Determine the sorting order:
        - If the sum is odd, sort the array in ascending order
        - If the sum is even, sort the array in descending order
    
    5. Sort the array:
        - Use the sort() method to sort the copied array
        - Pass the appropriate sorting order as an argument (True for ascending, False for descending)
    
    6. Return the sorted array:
        - Return the sorted copy of the input array
        - Ensure the original array remains unchanged
    """
    array_copy = array.copy()
    sum_first_last = array_copy[0] + array_copy[-1]
    if sum_first_last % 2 == 0:
        array_copy.sort(reverse=True)
    else:
        array_copy.sort()
    return array_copy