
from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.

    Args:
    l (List[int]): A list of integers

    Returns:
    int: The maximum element in the list

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        return None
    max_element = l[0]
    for element in l:
        if element > max_element:
            max_element = element
    return max_element