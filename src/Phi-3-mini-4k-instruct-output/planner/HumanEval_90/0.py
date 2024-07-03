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
    1. Check if the input list is empty:
        - If true, return None
    
    2. Find the smallest element in the list:
        - Use a loop or a built-in function to find the minimum value
    
    3. Remove the smallest element from the list:
        - Use a method to remove the smallest element from the list
    
    4. Check if the list still has elements:
        - If true, find the second smallest element in the remaining list
        - If false, return None (no second smallest element)
    
    5. Return the second smallest element
    
    Note: Consider using built-in functions or methods to simplify the implementation.
    Be careful when removing elements from the list to avoid index errors.
    """
    if not lst:
        return None
    
    smallest = min(lst)
    lst.remove(smallest)
    
    if not lst:
        return None
    
    second_smallest = min(lst)
    return second_smallest