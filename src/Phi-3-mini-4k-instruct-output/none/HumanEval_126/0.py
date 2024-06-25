def is_sorted(lst):
    """
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    :param lst: List of integers
    :return: Boolean indicating if the list is sorted and has no duplicates
    """
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        return True

    # Check for duplicates
    if len(lst) != len(set(lst)):
        return False

    # Check if the list is sorted
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True