def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Args:
        lst (List[int]): A non-empty list of integers.

    Returns:
        int: The sum of the even elements at odd indices.

    Examples:
        >>> add([4, 2, 6, 7])
        2
    """
    # Step 2: Initialize a variable to store the sum
    sum_even_at_odd_indices = 0

    # Step 3: Iterate through the list with a step of 2
    for i in range(0, len(lst), 2):
        # Step 4: Check for even elements at odd indices
        if lst[i] % 2 == 0 and i % 2 != 0:
            # Step 5: Add the even elements to the sum
            sum_even_at_odd_indices += lst[i]

    # Step 6: Return the final sum
    return sum_even_at_odd_indices