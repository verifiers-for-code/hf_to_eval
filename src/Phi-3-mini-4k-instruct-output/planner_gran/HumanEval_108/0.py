def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
    1. Initialize a counter variable to store the count of numbers with a sum of digits greater than 0
       - Set the counter to 0 initially
    
    2. Iterate through each number in the input array:
       a. Check if the current number is negative:
          - If negative, convert it to its positive equivalent by negating it (e.g., -123 becomes 123)
       b. Calculate the sum of digits for the current number:
          - Convert the number to a string to easily access individual digits
          - Use a loop or generator expression to iterate over each digit
          - Convert each digit back to an integer and sum them up
       c. Check if the sum of digits is greater than 0:
          - If true, increment the counter
    
    3. After iterating through all numbers, return the counter value
       - This represents the number of elements with a sum of digits greater than 0
    
    Additional implementation details:
    - Use a for loop or list comprehension to iterate over the input array
    - Use the appropriate string and integer methods for converting numbers to strings and back to integers
    - Consider using a conditional expression or if-else statement to handle the case where the input array is empty
    - Ensure the function handles edge cases, such as an empty input array or a list with only negative numbers
    """
    count = 0
    for num in arr:
        if num < 0:
            num = -num
        digit_sum = sum(int(digit) for digit in str(num))
        if digit_sum > 0:
            count += 1
    return count