from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
    Action Plan:
    1. Check if the list of numbers is empty or contains only one element:
        a. If true, return the input list as is (because the rolling max for a single element or an empty list is itself)
    
    2. Initialize an empty result list with the first element of the input list:
        a. result = [numbers[0]]
    
    3. Iterate over the input list starting from the second element:
        a. For each index (i) from 1 to the length of numbers - 1:
            i. Initialize a variable 'max_so_far' to numbers[i] (the current element itself)
            ii. Iterate over the sublist from index 0 to i (inclusive):
                1. If any element in the sublist is greater than 'max_so_far', update 'max_so_far'
            iii. Append 'max_so_far' to the result list
    
    4. Return the result list after completing the iteration
    """
    if len(numbers) <= 1:
        return numbers

    result = [numbers[0]]
    for i in range(1, len(numbers)):
        max_so_far = numbers[i]
        for j in range(i):
            if numbers[j] > max_so_far:
                max_so_far = numbers[j]
        result.append(max_so_far)
    return result