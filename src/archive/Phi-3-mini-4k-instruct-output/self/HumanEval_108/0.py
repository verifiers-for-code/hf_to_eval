def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    """
    def sum_of_digits(num):
        """
        Helper function to calculate the sum of digits with signed digit rule for negatives
        """
        if num == 0:
            return 0
        elif num < 0:
            num = -num
            return sum(int(digit) for digit in str(num))
        else:
            return sum(int(digit) for digit in str(num))

    return sum(1 for num in arr if sum_of_digits(num) > 0)