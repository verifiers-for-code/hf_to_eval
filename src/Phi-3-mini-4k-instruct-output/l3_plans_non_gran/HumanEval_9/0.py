from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    

    Action Plan:
    1. Understand the problem:
        - The function takes a list of integers as input.
        - It should return a list of rolling maximum elements found until each moment in the sequence.
    
    2. Initialize variables:
        - `max_val` to store the maximum value encountered so far (initialize with negative infinity)
        - `rolling_max` to store the rolling maximum elements (initialize with an empty list)
    
    3. Iterate through the input list:
        - For each element in the input list:
            a. Check if the current element is greater than `max_val`
            b. If true, update `max_val` with the current element
            c. Append `max_val` to `rolling_max`
    
    4. Update the result:
        - Continue updating `max_val` and `rolling_max` for each element in the list
    
    5. Assemble the final result:
        - Return `rolling_max` as the final result
    
    Note: Be careful when handling the first element of the list, as it doesn't have a previous maximum to compare with."""
    
    max_val = float('-inf')
    rolling_max = []
    
    for num in numbers:
        if num > max_val:
            max_val = num
        rolling_max.append(max_val)
    
    return rolling_max