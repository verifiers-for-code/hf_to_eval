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
    1. Define a helper function to calculate the sum of digits for a number:
       - Handle both positive and negative numbers
       - Convert the number to a string to easily access its digits
       - Sum the digits, keeping the sign of the original number

    2. Use Python's sorted() function on the input list:
       - Provide a custom key function that uses the helper function
       - This ensures sorting based on the sum of digits
       - The original order is maintained for numbers with the same digit sum

    3. Return the sorted list
    """

    def sum_of_digits(num):
        """
        Helper function to calculate the sum of digits for a number.
        Handles both positive and negative numbers.
        """
        # Convert the number to a string to easily access its digits
        num_str = str(num)
        # Initialize the sum
        digit_sum = 0
        # Iterate through each character in the string
        for char in num_str:
            # Add the integer value of the character to the sum
            digit_sum += int(char)
        # Return the sum, keeping the sign of the original number
        return digit_sum if num >= 0 else -digit_sum

    # Use Python's sorted() function on the input list
    # Provide a custom key function that uses the helper function
    # This ensures sorting based on the sum of digits
    # The original order is maintained for numbers with the same digit sum
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))

    # Return the sorted list
    return sorted_nums