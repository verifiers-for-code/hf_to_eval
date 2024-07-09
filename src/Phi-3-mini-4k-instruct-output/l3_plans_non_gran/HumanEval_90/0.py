def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    

    Action Plan:
    1. Validate the input:
        - Check if the input is a list
        - Raise a TypeError if the input is not a list
    
    2. Handle edge cases:
        - Check if the list is empty
        - If empty, return None
    
    3. Sort the list in ascending order:
        - Use the built-in sorted() function to sort the list
    
    4. Check if the list has at least two elements:
        - If not, return None
    
    5. Return the 2nd smallest element:
        - Access the second element of the sorted list using indexing (lst[1])
    
    Note: Be careful with indexing, as Python uses 0-based indexing.
    Consider the possibility of duplicate elements in the list."""
    
    # Validate the input
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    # Handle edge cases
    if len(lst) == 0:
        return None
    
    # Sort the list in ascending order
    sorted_lst = sorted(lst)
    
    # Check if the list has at least two elements
    if len(sorted_lst) < 2:
        return None
    
    # Return the 2nd smallest element
    return sorted_lst[1]