def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    

    Action Plan:
    1. Define a function `get_positive` that takes a list `l` as input.
    2. Initialize an empty list to store the positive numbers.
    3. Iterate through each element `num` in the input list `l`:
        a. Check if `num` is greater than 0 (i.e., positive).
        b. If `num` is positive, add it to the new list.
    4. Return the new list containing only the positive numbers.
    5. Ensure the function handles lists with varying lengths and contents."""
    positive_numbers = []
    for num in l:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers