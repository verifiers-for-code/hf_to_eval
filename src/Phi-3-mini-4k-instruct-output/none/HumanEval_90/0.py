def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    """
    if len(lst) < 2:
        return None

    smallest = float('inf')
    second_smallest = float('inf')

    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest