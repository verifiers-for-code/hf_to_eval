def is_sorted(lst):
    """
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    :param lst: List of integers
    :return: Boolean value indicating if the list is sorted or not

    Examples:
    >>> is_sorted([5])
    True
    >>> is_sorted([1, 2, 3, 4, 5])
    True
    >>> is_sorted([1, 3, 2, 4, 5])
    False
    >>> is_sorted([1, 2, 3, 4, 5, 6])
    True
    >>> is_sorted([1, 2, 3, 4, 5, 6, 7])
    True
    >>> is_sorted([1, 3, 2, 4, 5, 6, 7])
    False
    >>> is_sorted([1, 2, 2, 3, 3, 4])
    True
    >>> is_sorted([1, 2, 2, 2, 3, 4])
    False
    """
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        return True

    # Iterate through the list and check if each element is greater than the next one
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    # Check for duplicates
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1] and lst.count(lst[i]) > 1:
            return False

    return True