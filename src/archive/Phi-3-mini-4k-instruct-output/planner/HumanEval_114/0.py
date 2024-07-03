def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    int: The minimum sum of any non-empty sub-array.
    
    Example:
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    """
    if not nums:  # Edge case: empty input array
        return 0

    min_sum = float('inf')  # Step 2: Initialize min_sum to maximum possible value
    curr_sum = 0  # Step 2: Initialize curr_sum to 0

    for num in nums:  # Step 3: Iterate through each element in the input array
        curr_sum += num  # Step 3a: Add the current element to curr_sum

        if curr_sum < min_sum:  # Step 3c: Update min_sum if curr_sum is less than min_sum
            min_sum = curr_sum

        if curr_sum < 0:  # Step 3b: Reset curr_sum to 0 if it becomes negative
            curr_sum = 0

    return min_sum  # Step 4: Return min_sum as the minimum sum of any non-empty sub-array