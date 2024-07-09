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
    1. Understand the problem requirements:
        - Given a positive integer n, create a pile of n levels of stones.
        - Each level has a specific number of stones.
        - The number of stones in each level is determined by the previous level.
    
    2. Initialize an empty list to store the pile of stones:
        - Create an empty list called `pile` to store the number of stones in each level.
    
    3. Calculate the number of stones for each level:
        - Iterate from 1 to n (inclusive) to calculate the number of stones for each level.
        - For each level, calculate the number of stones based on the previous level:
            - If the previous level has an odd number of stones, the current level has the next odd number.
            - If the previous level has an even number of stones, the current level has the next even number.
    
    4. Build the pile of stones:
        - Add the calculated number of stones to the `pile` list for each level.
    
    5. Return the final result:
        - Return the `pile` list, which contains the number of stones in each level."""
    
    pile = []
    for i in range(1, n+1):
        if i % 2 == 1:
            pile.append(i + 2)
        else:
            pile.append(i + 1)
    return pile