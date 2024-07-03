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
    1. Develop a helper function to calculate the sum of digits for each number:
        a. Handle both positive and negative numbers, making the first digit negative for negative inputs
        b. Convert the number to a list of digits and sum them
    
    2. In the main function:
        a. Generate a list of tuples with the original index and the sum of digits
        b. Sort the list based on the sum of digits, and in case of a tie, sort based on index
        c. Extract the sorted list of numbers from the sorted list of tuples
    
    3. Edge cases and performance considerations:
        a. An empty list input should yield an empty list
        b. Consider using the key parameter in the sorted() function for efficient sorting
        c. Optimization may be possible by utilizing a custom comparison for tuples in the sorting
    
    4. Test cases:
        a. Confirm that the function sorts numbers with the same digit sums correctly by index
        b. Validate the function for edge cases, such as an empty list, lists with negative numbers, and lists with the same digit sum
    
    5. Document the sorting criteria:
        a. Clearly state the order of precedence for sorting in comments for future reference
    
    6. Final evaluation:
        a. Ensure the output list is in the expected ascending order
        b. Double-check that the indices are correctly preserved where the digit sums have the same value
    """
    def sum_of_digits(n):
        """Helper function to calculate the sum of digits for a number."""
        # Convert the number to a string to handle negative numbers
        # and then to a list of digits.
        digits = [int(d) for d in str(abs(n))]
        # If the number is negative, make the first digit negative.
        if n < 0:
            digits[0] *= -1
        return sum(digits)

    # Generate a list of tuples with the original index and the sum of digits.
    indexed_sums = [(i, sum_of_digits(num)) for i, num in enumerate(nums)]
    
    # Sort the list based on the sum of digits, and in case of a tie, sort based on index.
    sorted_indexed_sums = sorted(indexed_sums, key=lambda x: (x[1], x[0]))
    
    # Extract the sorted list of numbers from the sorted list of tuples.
    sorted_nums = [num for i, num in sorted_indexed_sums]
    
    return sorted_nums