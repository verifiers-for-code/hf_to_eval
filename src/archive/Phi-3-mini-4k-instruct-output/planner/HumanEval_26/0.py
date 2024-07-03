from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Parameters:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with duplicates removed, preserving the original order.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    unique_numbers = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            unique_numbers.append(number)

    return unique_numbers