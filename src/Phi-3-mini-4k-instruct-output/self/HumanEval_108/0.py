def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    

    Action Plan:
    1. Identify and address the problem's requirements:
        a. Handle positive and negative numbers
        b. Calculate the sum of digits with a signed digit rule for negatives
    
    2. Develop a helper function to calculate the sum of digits:
        a. Define a function to separate the negative and positive parts of the number
        b. Apply signed digit rules for negative numbers
        c. Convert the number to a string and sum the digits
    
    3. Implement the main function using list comprehension:
        a. Use a helper function to process each number in the input array
        b. Apply conditions to consider the sum of digits > 0
    
    4. Cover edge cases:
        a. An empty array
        b. Arrays with all negative or zero numbers
    
    5. Optimize and validate:
        a. Ensure the plan respects the signed digit rule efficiently
        b. Check the solution against the provided test cases and additional edge cases
    
    6. Emphasize the importance of modularization and readability, which helps in maintaining and improving the codebase in the future.
    """
    def sum_of_digits(num):
        """
        Helper function to calculate the sum of digits with a signed digit rule for negatives.
        """
        # Separate the negative and positive parts of the number
        if num < 0:
            num = -num
        sign = -1 if num < 0 else 1
        num = abs(num)
        
        # Convert the number to a string and sum the digits
        return sum(int(digit) for digit in str(num)) * sign

    # Implement the main function using list comprehension
    return sum(1 for num in arr if sum_of_digits(num) > 0)