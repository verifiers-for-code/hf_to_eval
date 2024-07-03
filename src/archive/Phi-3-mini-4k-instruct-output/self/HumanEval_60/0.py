def sum_to_n(n: int) -> int:
    """sum_to_n is a function that sums numbers from 1 to n.

    Args:
    n (int): The upper limit of the series.

    Returns:
    int: The sum of numbers from 1 to n.

    Examples:
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    # Step 2: Implement the formula
    result = n * (n + 1) // 2

    # Step 3: Address edge cases
    if n == 0:
        return 0

    # Step 4: Optimize
    # No need for iteration as the formula is direct and optimal

    return result