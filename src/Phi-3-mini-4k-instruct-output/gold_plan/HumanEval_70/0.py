def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []

    Action Plan:
    1. Initialize an empty result list and a boolean switch variable (True for minimum, False for maximum).
    2. While the input list is not empty:
       a. If switch is True, find the minimum value in the input list.
          If switch is False, find the maximum value in the input list.
       b. Append the found value to the result list.
       c. Remove the found value from the input list.
       d. Toggle the switch variable (change True to False or False to True).
    3. Return the result list.
    '''
    result = []
    switch = True

    while lst:
        if switch:
            min_val = min(lst)
            result.append(min_val)
            lst.remove(min_val)
        else:
            max_val = max(lst)
            result.append(max_val)
            lst.remove(max_val)
        switch = not switch

    return result