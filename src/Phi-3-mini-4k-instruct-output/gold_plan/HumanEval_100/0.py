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
    1. Initialize an empty list to store the number of stones for each level.
    2. Add the first level with n stones to the list.
    3. For each subsequent level (from 2 to n):
       a. Calculate the number of stones for the current level:
          - If n is odd, add 2 * (level - 1) to n
          - If n is even, add 2 * (level - 1) to n
       b. Add the calculated number to the list
    4. Return the final list containing the number of stones for each level

    Note: Consider using a loop or a list comprehension to generate the levels efficiently.
    """
    pile = [n]
    for level in range(1, n):
        if n % 2 == 0:
            stones = n + 2 * (level - 1)
        else:
            stones = n + 2 * (level - 1)
        pile.append(stones)
    return pile