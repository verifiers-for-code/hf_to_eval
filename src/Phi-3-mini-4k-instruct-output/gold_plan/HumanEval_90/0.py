def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    """
    # Step 1 & 2: Remove duplicates and sort the list
    unique_sorted_lst = sorted(set(lst))
    
    # Step 3: Check if the sorted list of unique elements has at least 2 items
    if len(unique_sorted_lst) < 2:
        return None
    
    # Step 4: Return the second element (index 1) of the sorted list
    return unique_sorted_lst[1]