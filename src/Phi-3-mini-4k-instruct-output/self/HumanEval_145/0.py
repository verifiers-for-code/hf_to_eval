def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    # Helper function to calculate the sum of digits
    def sum_of_digits(num):
        # Handle negative numbers by making the first digit negative
        num = abs(num)
        digits = [int(d) for d in str(num)]
        return -digits[0] + sum(digits[1:])

    # Generate a list of tuples with the original index and the sum of digits
    indexed_sums = [(i, sum_of_digits(num)) for i, num in enumerate(nums)]

    # Sort the list based on the sum of digits, and in case of a tie, sort based on index
    sorted_indexed_sums = sorted(indexed_sums, key=lambda x: (x[1], x[0]))

    # Extract the sorted list of numbers from the sorted list of tuples
    sorted_nums = [num for i, num in sorted_indexed_sums]

    return sorted_nums