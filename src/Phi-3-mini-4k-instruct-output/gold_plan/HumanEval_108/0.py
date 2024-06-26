def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    """
    def sum_of_digits(num):
        """
        Helper function to calculate the sum of digits for a number.
        Handles negative numbers by keeping track of the sign.
        """
        sign = -1 if num < 0 else 1
        num = abs(num)
        digits = [int(digit) for digit in str(num)]
        return sign * digits[0] + sum(digits[1:])

    # Handle the edge case of an empty array
    if not arr:
        return 0

    # Count how many numbers have a sum of digits greater than 0
    count = sum(1 for num in arr if sum_of_digits(num) > 0)

    return count