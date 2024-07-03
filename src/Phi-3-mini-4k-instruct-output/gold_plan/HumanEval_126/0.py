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

    Action Plan:
    1. Handle edge cases:
       - If the list is empty or has only one element, return True.

    2. Check for duplicates:
       - Create a dictionary to count occurrences of each number.
       - Iterate through the list, updating the count for each number.
       - If any number appears more than twice, return False.

    3. Check if the list is sorted:
       - Iterate through the list starting from the second element.
       - Compare each element with the previous one.
       - If any element is smaller than the previous one, return False.

    4. If all checks pass, return True.
    '''
    if len(lst) <= 1:
        return True

    num_counts = {}
    for num in lst:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    for num, count in num_counts.items():
        if count > 2:
            return False

    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False

    return True