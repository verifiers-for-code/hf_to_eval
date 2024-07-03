from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Step 2: Iterate through all possible combinations of three distinct elements in the list
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            for k in range(j + 1, len(l)):
                # Step 5: Check if l[i] + l[j] + l[k] equals 0
                if l[i] + l[j] + l[k] == 0:
                    # Step 6: If a combination summing to zero is found, immediately return True
                    return True
    # Step 7: If no combination is found after checking all possibilities, return False
    return False