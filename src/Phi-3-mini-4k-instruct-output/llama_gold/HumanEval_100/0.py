def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    

    Action Plan:
    1. Initialize an empty list to store the number of stones in each level.
    2. Recognize the pattern: the number of stones in each level is `n + 2*i`, where `i` starts from 0 and increments by 1 for each level.
    3. Iterate `n` times to generate the sequence of stone counts:
       a. Calculate the number of stones in the current level using the pattern.
       b. Append the calculated value to the list.
    4. Return the list containing the number of stones in each level, where the element at index `i` represents the number of stones in level `(i+1)`."""

    # Step 1: Initialize an empty list to store the number of stones in each level
    stone_counts = []

    # Step 2: Recognize the pattern
    for i in range(n):
        # Step 3a: Calculate the number of stones in the current level
        stones = n + 2*i

        # Step 3b: Append the calculated value to the list
        stone_counts.append(stones)

    # Step 4: Return the list containing the number of stones in each level
    return stone_counts