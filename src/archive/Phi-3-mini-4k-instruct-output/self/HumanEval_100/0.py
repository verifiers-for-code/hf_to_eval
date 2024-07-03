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
    # Step 1: Identify the base case
    if n == 1:
        return [n]

    # Step 2: Create a loop that iterates from the second level to n levels
    pile = [n]  # Initialize the pile with the first level
    current_stones = n
    for i in range(1, n):
        # Step 2a: Determine if n is odd or even
        if n % 2 == 0:
            # Step 2b: Update the number of stones in the current level based on the parity of n
            current_stones += 2
        else:
            # Step 2b: Update the number of stones in the current level based on the parity of n
            current_stones += 2 if current_stones % 2 == 0 else 1
        pile.append(current_stones)

    return pile