def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Step 1: Iterate through all possible pairs of numbers in the list
    for i, num1 in enumerate(l):
        for j in range(i + 1, len(l)):
            num2 = l[j]
            
            # Step 2: Check if the pair sums to zero
            if num1 + num2 == 0:
                return True
                
    # Step 3: If no pair sums to zero, return False
    return False