def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    

    Action Plan:
    1. Initialize two variables: min_sum to store the minimum sum of any sub-array and curr_sum to store the current sum of the sub-array.
    2. Set min_sum to the maximum possible value and curr_sum to 0.
    3. Iterate through each element in the input array nums:
        a. Add the current element to curr_sum.
        b. If curr_sum is negative, reset it to 0.
        c. If curr_sum is less than min_sum, update min_sum with the current sum.
    4. After iterating through the entire array, return min_sum as the minimum sum of any non-empty sub-array.
    5. Consider edge cases, such as an empty input array or an array with all negative numbers.
    
    Note: Use a loop to iterate through the array and update the current sum and minimum sum accordingly.
    Be careful when handling the case when the current sum becomes negative."""
    
    if not nums:
        return 0
    
    min_sum = float('inf')
    curr_sum = 0
    
    for num in nums:
        curr_sum += num
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    
    return min_sum