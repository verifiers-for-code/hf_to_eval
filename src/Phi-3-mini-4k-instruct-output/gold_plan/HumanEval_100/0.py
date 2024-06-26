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
    """
    # Step 1: Initialize an empty list to store the number of stones for each level.
    stone_pile = []

    # Step 2: Add the first level with n stones to the list.
    stone_pile.append(n)

    # Step 3: For each subsequent level (from 2 to n):
    for level in range(2, n + 1):
        # a. Calculate the number of stones for the current level:
        if n % 2 == 0:  # If n is even
            stones = n + 2 * (level - 1)
        else:  # If n is odd
            stones = n + 2 * (level - 1) + 1

        # b. Add the calculated number to the list
        stone_pile.append(stones)

    # Step 4: Return the final list containing the number of stones for each level
    return stone_pile