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
    1. Define a helper function `sum_of_digits` to calculate the sum of digits of a number:
        a. Convert the number to a string to access individual digits
        b. Iterate through each digit, convert it back to an integer, and add it to the sum
        c. Return the total sum of digits
    
    2. Define the main function `count_nums` to count numbers with a sum of digits > 0:
        a. Initialize a counter variable to store the count
        b. Iterate through each number in the input array
        c. For each number, check if it's negative:
            - If negative, calculate the sum of its signed digits using the `sum_of_digits` function
            - If the sum is greater than 0, increment the counter
        d. After iterating through all numbers, return the final count
    
    3. Consider handling edge cases, such as an empty input array or a single-element array
    
    4. Test the function with various input arrays to ensure it produces the correct output
    """
    def sum_of_digits(num):
        """
        Helper function to calculate the sum of digits of a number.
        If the number is negative, its first signed digit will be negative.
        """
        if num == 0:
            return 0
        sign = -1 if num < 0 else 1
        num = abs(num)
        sum_digits = 0
        while num > 0:
            sum_digits += sign * (num % 10)
            num //= 10
        return sum_digits

    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count