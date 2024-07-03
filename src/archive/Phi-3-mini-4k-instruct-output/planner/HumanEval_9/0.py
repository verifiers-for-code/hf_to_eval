from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    
    Args:
    numbers (List[int]): A list of integers
    
    Returns:
    List[int]: A list of rolling maximum elements found until a given moment in the sequence
    
    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [numbers[0]]  # Step 2: Initialize the result list and a variable to store the rolling maximum
    rolling_max_value = numbers[0]  # Step 2: Initialize the rolling maximum, set to the first element of the input list

    # Step 3: Iterate through the input list
    for i in range(1, len(numbers)):
        # Step 4: Update the rolling maximum and append it to the result list
        if numbers[i] > rolling_max_value:
            rolling_max_value = numbers[i]
        result.append(rolling_max_value)

    # Step 5: Return the final result
    return result