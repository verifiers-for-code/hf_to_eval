from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    max_value = numbers[0]
    rolling_max_list.append(max_value)
    
    for num in numbers[1:]:
        max_value = max(max_value, num)
        rolling_max_list.append(max_value)
    
    return rolling_max_list