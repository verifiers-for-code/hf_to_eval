def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    

    1. Understand the input:
       - The function takes a list (l) as input
       - The list can contain any type of elements (integers, floats, etc.)
    
    2. Increment each element:
       - Use a list comprehension to iterate over each element in the list
       - Increment each element by 1
       - This can be done using a list comprehension
    
    3. Return the modified list:
       - After incrementing all elements, return the modified list
       - The returned list should have the same length as the input list, with each element incremented by 1
    
    Additional implementation details:
    - Consider using a list comprehension for a concise and efficient implementation
    - Ensure the function handles empty lists correctly (return an empty list)
    - Verify that the function works with lists containing different types of elements (integers, floats, etc.)
    - Test the function with various input lists to ensure it produces the correct output"""
    return [x + 1 for x in l]