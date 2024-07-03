def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    

    1. Define a helper function to calculate the sum of digits:
       - Name the function sum_of_digits
       - Take an integer as input
       - Convert the integer to a string
       - Iterate over each character in the string
       - Convert each character back to an integer and sum them up
       - Return the sum of digits
    
    2. Create a sorting key that combines the sum of digits and the original index:
       - Define a lambda function as the key for the sorted function
       - The lambda function should take an integer as input
       - Calculate the sum of digits for the input integer using the sum_of_digits function
       - Add the original index of the input integer (use the index method of the list)
       - Return the sum of digits and the original index as a tuple
    
    3. Use the sorted function to sort the list:
       - Pass the input list to the sorted function
       - Use the lambda function as the key for sorting
       - The sorted function will sort the list based on the sum of digits and the original index
    
    4. Return the sorted list:
       - Assign the sorted list to a variable
       - Return the sorted list
    
    Additional implementation details:
    - Ensure the sum_of_digits function handles single-digit integers correctly
    - Use the appropriate method to get the original index of an integer in the list
    - Consider handling edge cases, such as an empty input list"""

    def sum_of_digits(n):
        return sum(int(digit) for digit in str(abs(n)))

    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))