def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Step 1: Initialize two variables
    max_sum = 0
    current_sum = 0

    # Step 2: Iterate through each number in the input array 'nums'
    for num in nums:
        # a. Negate the current number
        negated_num = -num

        # b. Add the negated number to current_sum
        current_sum += negated_num

        # c. If current_sum becomes negative, reset it to 0
        if current_sum < 0:
            current_sum = 0

        # d. Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)

    # Step 3: Check if max_sum is still 0
    if max_sum == 0:
        # If it is, find the maximum of the negated numbers in the array
        return max(nums)

    # Step 4: Calculate the final result
    # The minimum sum of the original array is the negative of max_sum
    return -max_sum