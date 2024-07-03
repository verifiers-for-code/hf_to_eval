def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    # Handle edge cases
    if len(lst) <= 1:
        return True

    # Check for duplicates
    num_counts = {}
    for num in lst:
        if num in num_counts:
            num_counts[num] += 1
            if num_counts[num] > 2:
                return False
        else:
            num_counts[num] = 1

    # Check if the list is sorted
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False

    return True