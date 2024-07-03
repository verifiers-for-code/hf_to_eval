def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]

    Action Plan:
    1. Convert the input list to a data structure that automatically removes duplicates.
       Hint: Think of a collection type in Python that only stores unique elements.

    2. Convert the result back to a list.
       Hint: Use a built-in function to create a list from the collection you used in step 1.

    3. Sort the list in ascending order.
       Hint: Use a built-in function that sorts lists.

    4. Return the sorted list of unique elements.

    Remember: Try to use efficient, built-in Python functions for each step.
    The entire operation can be done in a single line, but break it down into steps for clarity.
    """
    # Step 1: Convert the input list to a set to remove duplicates
    unique_elements = set(l)
    
    # Step 2: Convert the set back to a list
    unique_elements_list = list(unique_elements)
    
    # Step 3: Sort the list in ascending order
    unique_elements_list.sort()
    
    # Step 4: Return the sorted list of unique elements
    return unique_elements_list