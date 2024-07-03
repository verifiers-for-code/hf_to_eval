def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    

    1. Initialize variables:
       - min_sum: Initialize with a very large value (e.g., positive infinity) to ensure any sum will be smaller
       - current_sum: Initialize with 0 to keep track of the sum of the current sub-array
    
    2. Iterate through the input array:
       - For each number in the array:
         a. Add the current number to the current_sum
         b. If the current_sum becomes negative:
            - Reset current_sum to 0 (start a new sub-array)
         c. Update min_sum if the current_sum is smaller
    
    3. After iterating through the entire array:
       - Return min_sum as the minimum sum of any non-empty sub-array
    
    Additional implementation details:
    - Use a loop to iterate through the input array
    - Use conditional statements to update the current_sum and min_sum variables
    - Ensure the function handles edge cases, such as an empty input array or an array with a single element
    - Consider using a more efficient algorithm, such as Kadane's algorithm, for larger input arrays"""
    if not nums:
        return 0
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > 0:
            current_sum = 0
    return min_sum