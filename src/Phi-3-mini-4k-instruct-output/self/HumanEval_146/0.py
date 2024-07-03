def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
    Action Plan:
    1. Iterate through the input array of numbers
    2. For each number, check if it's greater than 10
    3. For numbers that pass the first check, extract the first and last digits
    4. Ensure the first and last digits are odd (1, 3, 5, 7, 9)
    5. Count the numbers that meet all the criteria
    6. Return the count as the final result
    
    Considerations:
    - Handle negative numbers by accessing the first and last digits appropriately
    - Assume single-digit numbers cannot have a 'last' digit
    - Edge cases: array with no numbers greater than 10 or both odd first and last digits
    
    Optimization Tip:
    - Avoid unnecessary transformations of the input numbers; work with the digits directly if possible"""

    def is_odd(digit):
        return digit in [1, 3, 5, 7, 9]

    count = 0
    for num in nums:
        if num > 10:
            str_num = str(num)
            if len(str_num) > 1:
                first_digit = int(str_num[0])
                last_digit = int(str_num[-1])
                if is_odd(first_digit) and is_odd(last_digit):
                    count += 1
    return count