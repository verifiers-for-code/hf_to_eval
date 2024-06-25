def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, they are ordered based on their index in the original list.

    :param nums: List of integers
    :return: Sorted list of integers

    Example:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """
    # Helper function to calculate the sum of digits of a number
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(abs(n)))

    # Sort the list using a custom key
    nums.sort(key=lambda x: (sum_of_digits(x), nums.index(x)))

    return nums