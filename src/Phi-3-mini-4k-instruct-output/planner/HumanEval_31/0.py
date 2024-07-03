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
    1. Handle edge cases:
        - Check if the input number n is less than or equal to 1
        - If true, return False (not prime)
    
    2. Implement the primality test:
        - Initialize a loop to check for factors of n
        - Iterate from 2 to the square root of n (inclusive)
        - For each iteration, check if n is divisible by the current number
        - If a divisor is found, return False (not prime)
    
    3. Optimize the algorithm:
        - Use the square root of n as the upper limit for the loop
        - This reduces the number of iterations needed
    
    4. Return the result:
        - If no divisors are found, return True (prime)
        - Otherwise, return False (not prime)
    
    Note: Consider using a more efficient algorithm for large numbers, such as the Sieve of Eratosthenes."""
    
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True