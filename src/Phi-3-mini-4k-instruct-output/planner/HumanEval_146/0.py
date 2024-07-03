def specialFilter(nums):
    """
    Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    
    Parameters:
    nums (list): A list of integers.
    
    Returns:
    int: The number of elements in the input list that meet the criteria.
    
    Action Plan:
    1. Define the function `specialFilter` with a single parameter `nums`, which is an array of numbers.
    2. Initialize a variable `count` to store the number of elements that meet the criteria.
    3. Iterate through each number in the input array `nums`:
        a. Extract the first and last digits of the current number.
        b. Check if both digits are odd (1, 3, 5, 7, 9).
        c. Check if the number is greater than 10.
        d. If both conditions are met, increment the `count` variable.
    4. After iterating through all numbers, return the final `count` value.
    5. Consider adding a docstring to explain the function's purpose, parameters, and return value.
    
    Note: Use appropriate string and integer operations to extract digits and perform comparisons.
    Be careful with the indexing when extracting the first and last digits.
    """
    count = 0
    for num in nums:
        first_digit = abs(num) % 10
        last_digit = abs(num) // 10 % 10
        if first_digit % 2 == 1 and last_digit % 2 == 1 and num > 10:
            count += 1
    return count