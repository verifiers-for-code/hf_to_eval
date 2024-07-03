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
    1. Define a helper function to calculate the sum of digits for a single number:
       a. Check if the number is negative, and if so, convert it to positive and store the sign.
       b. Convert the number to a list of digits (as strings) and then to integers.
       c. Apply the sign to the first digit if the original number was negative.
       d. Return the sum of the digits.
    2. Apply the helper function to each element in the input array:
       a. Use a list comprehension to calculate the sum of digits for each element.
    3. Count the number of elements with a sum of digits greater than 0:
       a. Use a filtering mechanism (e.g., filter or list comprehension) to select sums greater than 0.
       b. Return the count of these elements.
    """
    def sum_of_digits(num):
        # Check if the number is negative, and if so, convert it to positive and store the sign
        sign = -1 if num < 0 else 1
        num = abs(num)
        
        # Convert the number to a list of digits (as strings) and then to integers
        digits = [int(d) for d in str(num)]
        
        # Apply the sign to the first digit if the original number was negative
        if sign == -1:
            digits[0] *= sign
        
        # Return the sum of the digits
        return sum(digits)
    
    # Apply the helper function to each element in the input array
    sums = [sum_of_digits(num) for num in arr]
    
    # Count the number of elements with a sum of digits greater than 0
    return sum(1 for s in sums if s > 0)