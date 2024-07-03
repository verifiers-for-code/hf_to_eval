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
    1. Start by creating a copy of the input array to avoid altering the original array.
        a. Use slicing or a list comprehension to create a duplicate array
    
    2. Define a helper function to determine the sorting order based on the sum of the first and last elements:
        a. Calculate the sum of the first and last elements of the array
        b. Return 'ascending' if the sum is odd, and 'descending' if it's even
    
    3. Implement the main sorting logic using conditional statements:
        a. Check the sorting order from the helper function
        b. If ascending, use an appropriate sorting method (e.g., `sort()`)
        c. If descending, use `sort(reverse=True)`
    
    4. Ensure the solution includes testing with provided examples and edge cases:
        a. Empty array
        b. Single-element array
        c. Both odd and even sums
    
    5. Enhance the solution with efficient practices, such as minimizing computations inside loops."""
    
    # Step 1: Create a copy of the input array
    array_copy = array[:]
    
    # Step 2: Define a helper function to determine the sorting order
    def determine_sort_order(arr):
        return 'ascending' if (arr[0] + arr[-1]) % 2 != 0 else 'descending'
    
    # Step 3: Implement the main sorting logic
    sort_order = determine_sort_order(array_copy)
    if sort_order == 'ascending':
        array_copy.sort()
    else:
        array_copy.sort(reverse=True)
    
    # Step 4: Testing with provided examples and edge cases
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    
    # Step 5: Enhance the solution with efficient practices
    # (Already implemented by using list slicing and avoiding unnecessary computations)
    
    return array_copy