def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2

    Action Plan:
    1. Initialize a counter variable to keep track of numbers meeting the criteria.
    2. Iterate through each number in the input array 'nums'.
    3. For each number, check if it's greater than 10.
    4. If the number is greater than 10:
       a. Convert the number to a string.
       b. Check if the first character (index 0) of the string is an odd digit.
       c. Check if the last character (index -1) of the string is an odd digit.
       d. If both first and last digits are odd, increment the counter.
    5. After the iteration, return the final count.

    Note: Remember to handle potential edge cases, such as negative numbers.
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(num)
            if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count