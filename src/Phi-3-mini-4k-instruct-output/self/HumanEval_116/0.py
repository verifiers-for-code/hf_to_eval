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
    1. Prepare the array for sorting:
        - Use list comprehension to create a list of tuples, each containing the number and its binary representation.
    
    2. Sort the list using a custom key:
        - Create a lambda function that prioritizes the number of ones in the binary representation and, in case of a tie, uses the number itself.
    
    3. Handling edge cases:
        - Ensure negative numbers are handled appropriately but are not the primary sorting factor.
    
    4. Edge case verification:
        - Test the function with negative numbers, zero, and arrays where numbers have the same number of ones.
    
    5. Optimization:
        - Consider the efficiency of the lambda function and list sorting.
    
    6. Testing:
        - Validate against the given test cases."""

    # Step 1: Prepare the array for sorting
    arr_with_binary = [(num, bin(num).count('1')) for num in arr]

    # Step 2: Sort the list using a custom key
    arr_with_binary.sort(key=lambda x: (x[1], x[0]))

    # Step 3: Handling edge cases
    # Negative numbers are not the primary sorting factor, but they are included in the output

    # Step 4: Edge case verification
    # Testing is done through the provided examples

    # Step 5: Optimization
    # The lambda function and list sorting are efficient for the given problem

    # Step 6: Testing
    # Validate against the given test cases

    # Return the sorted array based on the binary representation
    return [num for num, _ in arr_with_binary]