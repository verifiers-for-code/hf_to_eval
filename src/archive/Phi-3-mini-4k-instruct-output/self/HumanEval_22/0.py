from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    def is_integer(value: Any) -> bool:
        """Check if the given value is an integer (including negative integers)"""
        return isinstance(value, int)

    filtered_integers = [value for value in values if is_integer(value)]
    return filtered_integers