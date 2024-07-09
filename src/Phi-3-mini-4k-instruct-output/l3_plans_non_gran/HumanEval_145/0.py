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
    1. Define a helper function `sum_of_digits` that takes an integer as input and returns the sum of its digits.
        - Convert the number to a string to iterate over its digits
        - Initialize a variable to store the sum of digits
        - Iterate over each digit in the string:
            - Convert the digit back to an integer
            - Add the integer to the sum
        - Return the sum of digits
    
    2. Use the `sorted` function to sort the input list `nums`.
        - Pass the `sum_of_digits` function as the `key` parameter to the `sorted` function.
        - This will sort the list based on the sum of digits for each number.
    
    3. Since the `sorted` function is stable, it will handle the case where multiple numbers have the same sum of digits.
        - The order of these numbers will be determined by their original index in the list.
    
    4. Return the sorted list.
    
    Note: The `sorted` function returns a new list and does not modify the original list.
    Make sure to handle the case where the input list is empty.
    """
    def sum_of_digits(num):
        """
        Helper function to calculate the sum of digits of a number.
        """
        return sum(int(digit) for digit in str(abs(num)))

    # Sort the list using the sum_of_digits as the key
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))

    return sorted_nums