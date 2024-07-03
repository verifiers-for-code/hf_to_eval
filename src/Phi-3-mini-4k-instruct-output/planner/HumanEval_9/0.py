from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    

    Action Plan:
    1. Understand the problem:
        - The function takes a list of integers as input
        - It returns a list of rolling maximum elements found until a given moment in the sequence
    
    2. Initialize the result list and a variable to store the rolling maximum:
        - Create an empty list to store the rolling maximum elements
        - Initialize a variable to store the rolling maximum, set to the first element of the input list
    
    3. Iterate through the input list:
        - Start from the second element of the input list (index 1)
        - For each element, compare it with the current rolling maximum
    
    4. Update the rolling maximum and append it to the result list:
        - If the current element is greater than the rolling maximum, update the rolling maximum
        - Append the rolling maximum to the result list
    
    5. Return the final result:
        - After iterating through the entire input list, return the result list
    
    Note: Use a loop to iterate through the input list and update the rolling maximum accordingly.
    Be careful when updating the rolling maximum and appending it to the result list."""
    
    result = []
    rolling_max_value = numbers[0]
    
    for num in numbers[1:]:
        if num > rolling_max_value:
            rolling_max_value = num
        result.append(rolling_max_value)
    
    return result