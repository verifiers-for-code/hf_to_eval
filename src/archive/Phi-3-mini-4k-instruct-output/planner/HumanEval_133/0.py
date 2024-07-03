def sum_squares(lst):
    """
    You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    
    Action Plan:
    1. Initialize a variable to store the sum of squared numbers.
    2. Iterate through each element in the input list:
        a. Round the current element to the upper int(Ceiling) using the int() function.
        b. Square the rounded element using the ** operator.
        c. Add the squared element to the sum variable.
    3. After processing all elements, return the sum of squared numbers.
    
    Note: Be careful when rounding the elements to the upper int(Ceiling) to ensure correct results.
    Use the int() function to perform the rounding operation.
    """
    sum_squared = 0
    for num in lst:
        rounded_num = int(num + 0.5)  # rounding to the upper int(Ceiling)
        squared_num = rounded_num ** 2
        sum_squared += squared_num
    return sum_squared