from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of numbers.
    threshold (float): The threshold value.

    Returns:
    bool: True if any two numbers in the list are closer to each other than the given threshold, False otherwise.

    Examples:
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    result = False
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                result = True
                break
        if result:
            break
    return result