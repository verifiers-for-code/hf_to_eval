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
    

    1. Define a helper function `is_prime(n)`:
       - This function takes an integer `n` as input
       - It returns `True` if `n` is prime, `False` otherwise
       - Implement the prime number check using a loop or other method
    
    2. Initialize variables to store the largest prime number and its sum of digits:
       - Initialize `largest_prime` to 0
       - Initialize `largest_prime_sum` to 0
    
    3. Iterate through each number in the input list:
       a. Check if the current number is prime using the `is_prime(n)` function
       b. If the number is prime:
          - Update `largest_prime` if the current number is greater
          - Calculate the sum of the digits of the current number
          - Update `largest_prime_sum` with the calculated sum
    
    4. Return the `largest_prime_sum` as the final result
    
    Additional implementation details:
    - In the `is_prime(n)` function, consider handling edge cases (e.g., `n <= 1`) and optimizing the prime number check
    - In the main loop, consider handling the case where no prime numbers are found in the list
    - Use appropriate variable names and comments to make the code readable and understandable"""

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = 0
    largest_prime_sum = 0

    for num in lst:
        if is_prime(num):
            if num > largest_prime:
                largest_prime = num
                largest_prime_sum = sum(int(digit) for digit in str(num))

    return largest_prime_sum