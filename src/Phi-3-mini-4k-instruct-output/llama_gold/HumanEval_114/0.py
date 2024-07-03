def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    

    Action Plan:
    1. Understand that the goal is to find the minimum sum of any non-empty sub-array in the given array of integers.
    2. Initialize two variables: one to store the maximum sum (max_sum) and one to store the current sum (s).
    3. Iterate through each number in the input array:
       a. Subtract the number from the current sum (since we want to find the minimum sum).
       b. If the current sum becomes negative, reset it to 0 (because a sub-array cannot have a negative sum).
       c. Update the maximum sum if the current sum is greater.
    4. After iterating through the entire array, if the maximum sum is still 0, it means all numbers are negative.
       a. In this case, find the maximum number in the array (which will be the minimum sum).
    5. Return the negative of the maximum sum, which represents the minimum sum of any non-empty sub-array."""
    
    max_sum = 0
    s = 0
    for num in nums:
        s += num
        if s < 0:
            s = 0
        max_sum = max(max_sum, s)
    
    if max_sum == 0:
        max_sum = max(nums)
    
    return -max_sum