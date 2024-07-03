def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    

    Action Plan:
    1. Define a helper function to calculate the sum of digits for a given number:
       a. Convert the number to its absolute value.
       b. Convert the number to a string and then to a list of digits.
       c. If the original number was negative, negate the first digit.
       d. Return the sum of the digits.
    2. Use the helper function as a key for sorting the input list.
    3. The built-in sorting function will automatically preserve the original order for items with similar sum of digits.
    4. Return the sorted list."""

    def sum_of_digits(num):
        """Helper function to calculate the sum of digits for a given number."""
        num = abs(num)
        digits = [int(d) for d in str(num)]
        if num < 0:
            digits[0] = -digits[0]
        return sum(digits)

    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))