def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6

    Action Plan:
    1. Initialize two variables:
       - max_sum: to keep track of the maximum sum (initially 0)
       - current_sum: to keep track of the current sum (initially 0)

    2. Iterate through each number in the input array 'nums':
       a. Negate the current number (multiply by -1)
       b. Add the negated number to current_sum
       c. If current_sum becomes negative, reset it to 0
       d. Update max_sum if current_sum is greater

    3. After the iteration, check if max_sum is still 0:
       - If it is, it means all numbers in the array were positive
       - In this case, find the maximum of the negated numbers in the array

    4. Calculate the final result:
       - The minimum sum of the original array is the negative of max_sum

    5. Return the final result
    """
    max_sum = 0
    current_sum = 0

    for num in nums:
        num = -num
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)

    if max_sum == 0:
        max_sum = max(nums)

    return -max_sum