def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # Step 1: Implement a filtering step for the first k elements of the array
    filtered_arr = [num for num in arr[:k]]

    # Step 2: Define a helper function to check if a number has at most two digits
    def has_at_most_two_digits(num):
        """Return True if the number has one or two digits, False otherwise."""
        abs_num = abs(num)
        num_str = str(abs_num)
        num_digits = len(num_str)
        return num_digits <= 2

    # Step 3: Apply the helper function to the filtered list
    valid_elements = [num for num in filtered_arr if has_at_most_two_digits(num)]

    # Step 4: Sum the numbers that meet the digit criteria
    result = sum(valid_elements)

    return result