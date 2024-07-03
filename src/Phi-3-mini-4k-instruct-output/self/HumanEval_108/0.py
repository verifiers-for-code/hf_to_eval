def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def sum_of_digits(num):
        """
        Helper function to calculate the sum of digits with a signed digit rule for negatives.
        """
        # Separate the negative and positive parts of the number
        if num < 0:
            num = -num
        # Convert the number to a string and sum the digits
        return sum(int(digit) for digit in str(num))

    # Use a list comprehension to process each number in the input array
    # Apply conditions to consider the sum of digits > 0
    return sum(1 for num in arr if sum_of_digits(num) > 0)