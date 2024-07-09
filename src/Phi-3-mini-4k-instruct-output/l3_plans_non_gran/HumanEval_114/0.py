def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    

    Action Plan:
    1. Initialize two variables: 
        - min_sum to store the minimum sum found so far (initialize with a large value, e.g., float('inf'))
        - current_sum to store the sum of the current sub-array (initialize with 0)
    
    2. Iterate through each element in the input array:
        a. Add the current element to current_sum
        b. If current_sum is less than min_sum, update min_sum with the new value
    
    3. After iterating through the entire array, return min_sum as the result
    
    Note: Be careful when initializing min_sum, as it should be a large value to ensure any sum in the array will be smaller.
    Use a variable to keep track of the current sum, and update it accordingly.
    Update min_sum only when a smaller sum is found.
    """
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum < min_sum:
            min_sum = current_sum
    return min_sum