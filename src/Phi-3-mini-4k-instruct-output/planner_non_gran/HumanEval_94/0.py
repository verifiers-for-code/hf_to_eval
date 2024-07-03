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
    1. Define a helper function `is_prime(n)` to check if a number `n` is prime:
        a. Handle edge cases: 0 and 1 are not prime
        b. Check divisibility from 2 to the square root of `n`
        c. Return `True` if `n` is prime, `False` otherwise
    
    2. Define a helper function `sum_of_digits(n)` to calculate the sum of digits of a number `n`:
        a. Convert `n` to a string
        b. Iterate through each character in the string
        c. Convert each character back to an integer and add to the sum
        d. Return the sum
    
    3. Implement the main function `skjkasdkd(lst)`:
        a. Initialize `max_prime` to 0 and `max_prime_index` to -1
        b. Iterate through each number `num` in the input list `lst`:
            i. Check if `num` is prime using `is_prime(num)`
            ii. If `num` is prime and greater than `max_prime`, update `max_prime` and `max_prime_index`
        c. If `max_prime` is not 0, calculate the sum of digits of `max_prime` using `sum_of_digits(max_prime)`
        d. Return the sum of digits of `max_prime`
    
    4. Handle edge cases and errors:
        a. Check for empty input lists
        b. Handle non-integer values in the input list
        c. Consider the case where no prime numbers are found in the list"""

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))

    if not lst:
        return "Error: Input list is empty."

    max_prime = 0
    max_prime_index = -1

    for index, num in enumerate(lst):
        if not isinstance(num, int):
            return "Error: Non-integer value found in the input list."
        if is_prime(num) and num > max_prime:
            max_prime = num
            max_prime_index = index

    if max_prime == 0:
        return "Error: No prime numbers found in the list."

    return sum_of_digits(max_prime)