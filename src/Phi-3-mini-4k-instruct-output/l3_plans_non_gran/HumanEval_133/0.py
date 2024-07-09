import math

def sum_squares(lst):
    """You are given a list of numbers.
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
        a. Round the current element to the upper int(Ceiling) using the math.ceil function.
        b. Square the rounded element.
        c. Add the squared element to the sum.
    3. After iterating through all elements, return the final sum.
    
    Note: Use the math module for the ceil function.
    Be careful when handling negative numbers and decimals."""
    
    sum_squared = 0
    for num in lst:
        rounded_num = math.ceil(num)
        squared_num = rounded_num ** 2
        sum_squared += squared_num
    return sum_squared