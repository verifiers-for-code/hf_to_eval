
from typing import List

def get_positive(l: List[int]) -> List[int]:
    """Return only positive numbers in the list.

    Args:
    l (List[int]): A list of integers.

    Returns:
    List[int]: A list containing only the positive integers from the input list.

    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in l if num > 0]