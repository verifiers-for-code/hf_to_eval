def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    

    Action Plan:
    1. Initialize a variable to store the count of numbers that meet the conditions.
    2. Iterate through each number in the input array:
        a. Check if the number is greater than 10.
        b. Extract the first and last digits of the number.
        c. Check if both the first and last digits are odd (1, 3, 5, 7, 9).
        d. If both conditions are met, increment the count variable.
    3. After iterating through the entire array, return the count of numbers that meet the conditions.
    
    Note: Use appropriate string manipulation and conditional statements to extract and compare the digits.
    Be careful to handle the case where the number has only one digit (i.e., the first and last digits are the same)."""
    count = 0
    for num in nums:
        if num > 10:
            str_num = str(num)
            if len(str_num) > 1:
                first_digit = int(str_num[0])
                last_digit = int(str_num[-1])
                if first_digit % 2 == 1 and last_digit % 2 == 1:
                    count += 1
            else:
                if int(str_num) % 2 == 1:
                    count += 1
    return count