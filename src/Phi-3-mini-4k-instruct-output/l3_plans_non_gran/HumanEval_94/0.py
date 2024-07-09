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
        a. Handle the edge case where `n` is less than 2
        b. Iterate from 2 to the square root of `n` and check for divisibility
        c. Return `True` if `n` is prime, `False` otherwise
    
    2. Initialize a variable `max_prime` to store the largest prime value found so far
    
    3. Iterate through each number `num` in the input list `lst`:
        a. Check if `num` is prime using the `is_prime` function
        b. If `num` is prime and greater than `max_prime`, update `max_prime` with `num`
    
    4. Calculate the sum of digits of `max_prime`:
        a. Initialize a variable `digit_sum` to 0
        b. Convert `max_prime` to a string to access individual digits
        c. Iterate through each character (digit) in the string and add it to `digit_sum`
    
    5. Return the final result, which is the sum of digits of the largest prime value"""

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = 0
    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num

    digit_sum = sum(int(digit) for digit in str(max_prime))

    return digit_sum