def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    

    Action Plan:
    1. Start with the function definition and its docstring, specifying the expected input and output.
    2. Initialize a variable to store the maximum element. Set it to the first element of the list by default.
    3. Iterate over the list using a loop, comparing each element to the current maximum element.
    4. Update the maximum element if a larger element is found during the iteration.
    5. After the loop completes, return the maximum element.
    
    6. Consider handling edge cases such as an empty list.
    7. Use Python's built-in max() function for an alternative, simpler approach.
    
    8. Test the function with the provided examples and additional cases to ensure correctness."""
    
    if not l:
        return None
    
    max_element = l[0]
    for element in l:
        if element > max_element:
            max_element = element
    return max_element