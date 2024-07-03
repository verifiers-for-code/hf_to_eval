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
    1. Check if the input list is empty. If so, return None.
    2. Remove duplicates from the list to ensure uniqueness of elements.
    3. Sort the list in ascending order.
    4. Check if the sorted list has at least two elements. If not, return None.
    5. Return the second element of the sorted list, which is the 2nd smallest element."""
    
    if not lst:
        return None
    
    lst = list(set(lst))
    lst.sort()
    
    if len(lst) < 2:
        return None
    
    return lst[1]