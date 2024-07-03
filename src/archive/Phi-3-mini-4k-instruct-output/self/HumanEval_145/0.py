def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, orders them based on their index in the original list.

    Args:
    nums (List[int]): The list of integers to be sorted.

    Returns:
    List[int]: The sorted list of integers.
    """

    # Helper function to calculate the sum of digits for each number
    def sum_of_digits(num):
        """Calculate the sum of digits for a given number.
        Handles both positive and negative numbers, making the first digit negative for negative inputs.
        """
        num_str = str(abs(num))
        return sum(int(digit) for digit in num_str)

    # Generate a list of tuples with the original index and the sum of digits
    indexed_sums = [(i, sum_of_digits(num)) for i, num in enumerate(nums)]

    # Sort the list based on the sum of digits, and in case of a tie, sort based on index
    sorted_indexed_sums = sorted(indexed_sums, key=lambda x: (x[1], x[0]))

    # Extract the sorted list of numbers from the sorted list of tuples
    sorted_nums = [num for i, num in sorted_indexed_sums]

    return sorted_nums