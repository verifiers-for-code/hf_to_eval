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
    1. Initialize a counter variable to store the number of elements with a sum of digits > 0.
    2. Iterate through each number in the input array:
        a. Convert the number to a string to access individual digits.
        b. Calculate the sum of the digits:
            - Use a loop or a generator expression to iterate through the digits.
            - Convert each digit back to an integer and add it to the sum.
            - If the number is negative, make the first digit negative (e.g., -123 becomes -1, 2, 3).
        c. Check if the sum of digits is greater than 0:
            - If true, increment the counter.
    3. After iterating through all numbers, return the final count.
    
    Note: Be careful when handling negative numbers to ensure correct signed digit calculation."""
    count = 0
    for num in arr:
        digits = [int(d) for d in str(abs(num))]
        if num < 0:
            digits[0] = -digits[0]
        if sum(digits) > 0:
            count += 1
    return count