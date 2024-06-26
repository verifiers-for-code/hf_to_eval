def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, they are ordered based on their index in the original list.

    Args:
    nums (List[int]): The list of integers to be sorted.

    Returns:
    List[int]: The sorted list of integers.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """

    # Step 1: Define a helper function to calculate the sum of digits for a number
    def sum_of_digits(num):
        """
        Calculates the sum of digits for a given number, preserving the sign of the original number.

        Args:
        num (int): The number to calculate the sum of digits for.

        Returns:
        int: The sum of digits for the given number.
        """
        num_str = str(abs(num))  # Convert the number to a string and get its absolute value
        return sum(int(digit) for digit in num_str) + (num < 0)  # Sum the digits and add the sign of the original number

    # Step 2: Use Python's sorted() function on the input list
    # Provide a custom key function that uses the helper function
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))

    # Step 3: Return the sorted list
    return sorted_nums