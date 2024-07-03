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
    1. Initialize an empty list to store the squared values
       - This list will hold the squared values of the rounded elements
    2. Iterate through each element in the input list:
       a. Round the current element to the upper int(Ceiling)
          - Use the appropriate function to round the element
       b. Square the rounded element
          - Use the exponentiation operator (**) to square the element
       c. Add the squared value to the list of squared values
    3. Calculate the sum of the squared values
       - Use the built-in sum function to add up all the squared values
    4. Return the final sum
       - The function should return the sum of the squared values as an integer
    
    Additional implementation details:
    - Use a loop or list comprehension to iterate through the input list
    - Use the appropriate function or operator to round each element to the upper int(Ceiling)
    - Use the exponentiation operator (**) to square each rounded element
    - Ensure that the function handles empty input lists correctly
    - Consider adding error handling for non-numeric input values
    """
    squared_values = []
    for num in lst:
        if isinstance(num, (int, float)):
            rounded_num = int(num + 1)
            squared_num = rounded_num ** 2
            squared_values.append(squared_num)
    return sum(squared_values)