def order_by_points(nums):
    """
    Sorts a given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, they are ordered based on their index in the original list.

    Args:
    nums (list): A list of integers.

    Returns:
    list: A sorted list of integers based on the sum of their digits and their original index.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """
    def sum_of_digits(num):
        """
        Calculates the sum of digits for a given number.

        Args:
        num (int): An integer.

        Returns:
        int: The sum of digits of the given number.
        """
        return sum(int(digit) for digit in str(abs(num)))

    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))