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
        return [1]

    # Step 2: Create a loop that iterates from the second level to n levels
    pile = [n]
    current_stones = n
    for i in range(1, n):
        # Step 3: Iteration logic
        if current_stones % 2 == 0:
            # If n is even, use the next even number
            current_stones += 2
        else:
            # If n is odd, use the next odd number
            current_stones += 2
        pile.append(current_stones)

    # Step 4: Edge cases
    # Handle negative numbers and non-integer inputs
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    # Step 5: Optimization
    # Keep track of the current odd or even number, avoiding redundant calculations
    # This step is already optimized in the current implementation

    # Step 6: Test the function
    # Verify against the given examples and test additional edge cases
    assert make_a_pile(3) == [3, 5, 7], "Test case failed: make_a_pile(3)"
    assert make_a_pile(1) == [1], "Test case failed: make_a_pile(1)"
    assert make_a_pile(0) == [], "Test case failed: make_a_pile(0)"
    print("All test cases passed.")

    return pile