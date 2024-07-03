def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    

    Action Plan:
    1. Initialize a counter to store the count of special numbers.
    2. Iterate through each number in the input array:
       a. Check if the number is greater than 10.
       b. If the number is greater than 10, convert it to a string to access its digits.
       c. Extract the first and last digits of the number from the string.
       d. Check if both the first and last digits are odd (1, 3, 5, 7, or 9).
       e. If the number meets all conditions, increment the counter.
    3. Return the count of special numbers that meet the conditions."""
    
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(num)
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 == 1 and last_digit % 2 == 1:
                count += 1
    return count