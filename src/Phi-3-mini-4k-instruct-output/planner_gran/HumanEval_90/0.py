def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    

    1. Handle edge cases:
       - Check if the input list is empty
       - If empty, return None immediately
       - Check if the list has only one element
       - If so, return None immediately
    
    2. Remove duplicates from the list:
       - Convert the list to a set to eliminate duplicates
       - Convert the set back to a list
    
    3. Sort the list in ascending order:
       - Use the built-in sorted() function to sort the list
    
    4. Return the second smallest element:
       - Since the list is sorted, the second element is the second smallest
       - Return this element as the result
    
    Additional implementation details:
    - Use the appropriate data structures and functions to handle edge cases and remove duplicates
    - Ensure the function returns None when there is no second smallest element
    - Consider using a more efficient sorting algorithm if the list is very large
    - Test the function with various input lists to ensure it works correctly
    """
    if not lst:
        return None
    if len(lst) == 1:
        return None
    lst = list(set(lst))
    lst.sort()
    if len(lst) < 2:
        return None
    return lst[1]