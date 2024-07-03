def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Step 1: Use a nested loop structure to iterate through all possible pairs of numbers in the list.
    for i, num1 in enumerate(l):
        for j in range(i+1, len(l)):
            num2 = l[j]
            # Step 2: For each pair of numbers, check if their sum is equal to zero.
            if num1 + num2 == 0:
                # If a pair sums to zero, immediately return True.
                return True
    # Step 3: If no pair sums to zero after checking all possibilities, return False.
    return False