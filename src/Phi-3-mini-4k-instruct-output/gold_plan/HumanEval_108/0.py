def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3

    Action Plan:
    1. Define a helper function to calculate the sum of digits for a number:
       a. Handle negative numbers by keeping track of the sign
       b. Convert the number to a string to easily access its digits
       c. Convert digits back to integers, applying the sign to the first digit if negative
       d. Return the sum of these digits

    2. In the main function:
       a. Handle the edge case of an empty array (return 0)
       b. Iterate through the input array:
          - For each number, calculate its sum of digits using the helper function
          - Count how many numbers have a sum of digits greater than 0
       c. Return the final count

    3. Consider using list comprehension or filter function for a more concise solution

    Note: Remember to handle both positive and negative numbers correctly
    """

    def sum_of_digits(num):
        """
        Helper function to calculate the sum of digits for a number.
        Handles negative numbers by keeping track of the sign.
        """
        sign = -1 if num < 0 else 1
        num = abs(num)
        digits = [int(digit) for digit in str(num)]
        digits[0] *= sign
        return sum(digits)

    # Handle the edge case of an empty array
    if not arr:
        return 0

    # Count numbers with a sum of digits greater than 0
    return sum(1 for num in arr if sum_of_digits(num) > 0)