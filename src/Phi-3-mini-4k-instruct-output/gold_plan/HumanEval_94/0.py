import math

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7

    Action Plan:
    1. Define a helper function `is_prime(n)` to check if a number is prime:
       a. If n is less than 2, return False
       b. Check for divisibility from 2 to sqrt(n)
       c. If no divisors found, return True

    2. Initialize a variable `largest_prime` to 0

    3. Iterate through each number in the input list:
       a. If the number is greater than `largest_prime` and is prime (use is_prime function):
          - Update `largest_prime` with this number

    4. Convert `largest_prime` to a string

    5. Sum the digits of the string:
       a. Initialize a sum variable to 0
       b. Iterate through each character in the string
       c. Convert the character to an integer and add to the sum

    6. Return the sum of digits

    Note: Handle the case where no prime number is found in the list (return 0 or appropriate value)
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = 0
    for num in lst:
        if num > largest_prime and is_prime(num):
            largest_prime = num

    if largest_prime == 0:
        return 0

    return sum(int(digit) for digit in str(largest_prime))