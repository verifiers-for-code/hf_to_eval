def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    

    Action Plan:
    1. Define the problem:
        - Given an array of integers, find the sum of the smallest non-empty sub-array
    
    2. Implement the sliding window technique:
        - Use two pointers to represent the start and end of the current sub-array
        - Slide the end pointer to expand the window
    
    3. Determine the sum of elements in the current window:
        - Increment the sum as the end pointer moves
    
    4. Once a sub-array is found, update the minimum sum found so far:
        - Compare the current sum with the minimum sum and update if necessary
    
    5. Slide the start pointer to reduce the window and check the next sub-array:
        - Continue until the end of the array is reached
    
    6. Handle edge cases:
        - Check for an empty array or array with a single element
    
    7. Return the minimum sum found
    
    8. Validate the solution:
        - Test with multiple examples and edge cases"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    min_sum = float('inf')
    current_sum = 0
    start = 0
    
    for end in range(len(nums)):
        current_sum += nums[end]
        
        while current_sum >= nums[start]:
            min_sum = min(min_sum, current_sum)
            current_sum -= nums[start]
            start += 1
    
    return min_sum