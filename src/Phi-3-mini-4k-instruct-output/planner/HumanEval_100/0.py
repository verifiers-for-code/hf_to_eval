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
    1. Check if n is equal to 1:
        - If true, return a list with a single element [1]
    2. Initialize an empty list to store the number of stones in each level
    3. Add the number of stones in the first level (n) to the list
    4. Initialize a variable to keep track of the current level (starting from 2)
    5. Loop until the current level exceeds n:
        a. Calculate the number of stones in the current level:
            - If the current level is odd, add the next odd number to the current level
            - If the current level is even, add the next even number to the current level
        b. Add the number of stones in the current level to the list
        c. Increment the current level by 1
    6. Return the list of stones in each level
    """
    if n == 1:
        return [1]
    stones = [n]
    current_level = 2
    while current_level <= n:
        if current_level % 2 == 0:
            stones.append(current_level + 1)
        else:
            stones.append(current_level + 2)
        current_level += 1
    return stones