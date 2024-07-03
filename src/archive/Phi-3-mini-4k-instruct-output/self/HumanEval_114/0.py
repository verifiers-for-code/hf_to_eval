def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    min_sum = float('inf')
    current_sum = 0
    start = 0

    for end in range(len(nums)):
        current_sum += nums[end]

        while current_sum >= min_sum:
            min_sum = min(min_sum, current_sum)
            current_sum -= nums[start]
            start += 1

    return min_sum