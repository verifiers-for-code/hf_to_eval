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
    1. Import a module that provides a function to calculate the ceiling of a number.
    2. Initialize a variable to store the sum of squared numbers, initially set to 0.
    3. Iterate through each element in the input list:
       a. Use the imported module to round the element to the upper integer (Ceiling).
       b. Square the rounded element.
       c. Add the squared value to the sum variable.
    4. After iterating through the entire list, return the sum of squared numbers."""
    
    total = 0
    for num in lst:
        total += math.ceil(num) ** 2
    return total