from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    

    Action Plan:
    1. Initialize a variable to store the running maximum value, initially set to None.
    2. Initialize an empty list to store the rolling maximum values.
    3. Iterate through each number in the input list:
       a. If the running maximum value is None, set it to the current number.
       b. Otherwise, update the running maximum value to be the maximum of the current number and the previous running maximum.
       c. Append the updated running maximum value to the result list.
    4. Return the result list containing the rolling maximum values."""
    
    running_max = None
    result = []
    
    for num in numbers:
        if running_max is None:
            running_max = num
        else:
            running_max = max(running_max, num)
        result.append(running_max)
    
    return result