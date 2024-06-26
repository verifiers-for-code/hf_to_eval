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
    1. Import the 'math' module to use the ceiling function.
    2. Initialize a variable (e.g., 'result') to 0 to store the sum of squared numbers.
    3. Iterate through each number in the input list 'lst'.
    4. For each number:
       a. Use math.ceil() to round it up to the nearest integer.
       b. Square the rounded number.
       c. Add the squared value to the 'result' variable.
    5. After the loop, return the 'result' variable containing the sum of squared numbers.
    """
    result = 0
    for num in lst:
        rounded_num = math.ceil(num)
        squared_num = rounded_num ** 2
        result += squared_num
    return result