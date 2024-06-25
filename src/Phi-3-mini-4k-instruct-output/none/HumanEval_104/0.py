def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all elements that haven't any even digit.

    Args:
    x (list): A list of positive integers.

    Returns:
    list: A sorted list of all elements that haven't any even digit.

    Example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result = []

    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            result.append(num)

    return sorted(result)