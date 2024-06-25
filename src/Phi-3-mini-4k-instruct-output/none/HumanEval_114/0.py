def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize variables
    min_sum = float('inf')
    current_sum = 0
    
    # Iterate through the list
    for num in nums:
        current_sum += num
        
        # If the current sum is less than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
        
        # If the current sum is greater than or equal to zero, reset the current sum
        if current_sum >= 0:
            current_sum = 0
    
    # If the minimum sum is still infinity, it means all elements are negative
    # In this case, return the minimum element
    if min_sum == float('inf'):
        return min(nums)
    
    return min_sum