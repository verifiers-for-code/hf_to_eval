from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Iterate through all possible combinations of three distinct elements in the list
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            for k in range(j + 1, len(l)):
                # Check if the sum of the three elements equals zero
                if l[i] + l[j] + l[k] == 0:
                    return True
    # If no combination is found after checking all possibilities, return False
    return False