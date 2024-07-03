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
    

    1. Initialize an empty list to store the number of stones in each level
       - This list will hold the result of the function
    
    2. Initialize a variable to keep track of the number of stones in the current level
       - This variable will be used to generate the number of stones for each level
    
    3. Create a loop to generate the list of stones:
       a. Loop `n` times, where `n` is the input parameter
       b. In each iteration:
          - Append the current number of stones to the list
          - Calculate the next number of stones based on the pattern:
             - If the current number of stones is odd, add 2 to get the next odd number
             - If the current number of stones is even, add 1 to get the next even number
          - Update the current number of stones for the next iteration
    
    4. Return the list of stones
       - The list now contains the number of stones in each level of the pile
    
    Additional implementation details:
    - Use a for loop to iterate `n` times
    - Use the modulus operator (%) to check if the current number of stones is odd or even
    - Use the append method to add the current number of stones to the list
    - Update the current number of stones correctly in each iteration
    - Ensure the function handles edge cases, such as `n` being 0 or 1"""
    
    pile = []
    current_stones = n
    
    for i in range(n):
        pile.append(current_stones)
        if current_stones % 2 == 0:
            current_stones += 1
        else:
            current_stones += 2
    
    return pile