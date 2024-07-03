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
    
    # Edge case: empty array
    if not nums:
        return 0
    
    # Edge case: array with a single element
    if len(nums) == 1:
        return nums[0]
    
    # Initialize pointers and variables
    start = 0
    end = 0
    current_sum = nums[0]
    min_sum = nums[0]
    
    # Iterate through the array
    while end < len(nums):
        # Slide the end pointer to expand the window
        current_sum += nums[end]
        
        # Update the minimum sum found so far
        if current_sum < min_sum:
            min_sum = current_sum
        
        # Slide the start pointer to reduce the window
        while current_sum >= min_sum and start < end:
            current_sum -= nums[start]
            start += 1
    
    return min_sum