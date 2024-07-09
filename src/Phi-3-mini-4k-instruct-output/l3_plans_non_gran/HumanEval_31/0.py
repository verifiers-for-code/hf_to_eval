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
        - If n is less than or equal to 1, return False (not prime)
    
    2. Understand the concept of prime numbers:
        - A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself
    
    3. Develop a loop to check divisibility:
        - Initialize a variable to 2 (the smallest prime number)
        - Loop until the square of the variable is less than or equal to n
        - In each iteration, check if n is divisible by the current variable
        - If n is divisible, return False (not prime)
    
    4. Optimize the loop:
        - Use a variable to keep track of the square of the current number
        - Increment the variable by 2 in each iteration (to check odd numbers)
        - Use the square root of n as the upper bound for the loop (to reduce unnecessary checks)
    
    5. Return the result:
        - If the loop completes without finding a divisor, return True (prime)
        - If a divisor is found, return False (not prime)
    
    Note: Consider using a more efficient algorithm for large numbers, such as checking divisibility up to the square root of n."""
    
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True