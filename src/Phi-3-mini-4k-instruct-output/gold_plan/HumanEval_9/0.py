from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]

    Action Plan:
    1. Initialize two variables:
       a. A variable to store the running maximum (initially None or the first element)
       b. An empty list to store the result

    2. Iterate through each number in the input list:
       a. If this is the first number (running max is None), set it as the running max
       b. Otherwise, compare the current number with the running max:
          - Update the running max if the current number is larger
       c. Append the current running max to the result list

    3. After the iteration, return the result list

    Note: Be careful with the initial case, especially if the list might be empty.
    """
    if not numbers:
        return []

    running_max = None
    result = []

    for num in numbers:
        if running_max is None:
            running_max = num
        else:
            running_max = max(running_max, num)
        result.append(running_max)

    return result