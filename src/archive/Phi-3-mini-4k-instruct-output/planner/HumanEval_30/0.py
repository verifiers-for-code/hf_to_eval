def get_positive(l: list):
    """Return only positive numbers in the list.

    Args:
    l (list): A list of integers.

    Returns:
    list: A list containing only the positive numbers from the input list.

    Examples:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # Step 2: Initialize an empty list to store the positive numbers
    positive_numbers = []

    # Step 3: Iterate through each number in the input list
    for num in l:
        # Step 3a: Check if the number is positive
        if num > 0:
            # Step 3b: If the number is positive, add it to the positive_numbers list
            positive_numbers.append(num)

    # Step 4: Return the list of positive numbers
    return positive_numbers