from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.

    Parameters:
    values (List[Any]): A list containing any Python values.

    Returns:
    List[int]: A list containing only the integer values from the input list.

    Example:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    filtered_integers = []
    for value in values:
        if isinstance(value, int):
            filtered_integers.append(value)
    return filtered_integers