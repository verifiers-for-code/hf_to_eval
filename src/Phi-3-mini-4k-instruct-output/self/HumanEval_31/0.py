import math

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    

    Action Plan:
    1. Identify the characteristics of a prime number:
        - Prime numbers are greater than 1
        - A prime number has no positive divisors other than 1 and itself
    
    2. Write a function to check if a given number 'n' is prime:
        a. Return False for n <= 1
        b. Check if 'n' is divisible by any number from 2 to the square root of 'n'
            - Use the fact that if 'n' has a factor greater than its square root, it must also have a smaller factor
    
    3. For the main logic:
        a. Start the loop from 2 and iterate up to (but not including) the square root of 'n'
        b. Use an efficient way to determine divisibility, such as the modulo operation
        c. Count and return the number of times 'n' is divisible (which should be 0 for prime numbers)
    
    4. Consider edge cases:
        a. Negative numbers and 0, which are not prime
        b. Small numbers where primality is easily checked by hand or a simple algorithm
    
    5. Optimization:
        a. Implement early exit conditions for small values and non-prime numbers to reduce unnecessary checks
    
    6. Testing:
        a. Verify the function with the given test cases and additional edge cases to ensure reliability and correctness"""

    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True