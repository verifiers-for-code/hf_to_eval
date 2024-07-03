def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Action Plan:
    1. Use a nested loop structure to iterate through all possible pairs of numbers in the list.
       - Outer loop: Use enumerate() to get both index and value of each element.
       - Inner loop: Use range() to iterate from the next index to the end of the list.
    
    2. For each pair of numbers:
       - Check if their sum is equal to zero.
       - If a pair sums to zero, immediately return True.
    
    3. If no pair sums to zero after checking all possibilities, return False.

    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for i, x in enumerate(l):
        for j in range(i+1, len(l)):
            if x + l[j] == 0:
                return True
    return False