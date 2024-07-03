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
    def sum_of_digits(n):
        """
        Calculates the sum of digits for a given number.
        Handles both positive and negative numbers.
        """
        str_n = str(abs(n))  # Convert the number to a string to easily access its digits
        return sum(int(digit) for digit in str_n) + (n < 0)  # Sum the digits and keep the sign of the original number

    # Step 2: Use Python's sorted() function on the input list
    # Provide a custom key function that uses the helper function
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))

    # Step 3: Return the sorted list
    return sorted_nums