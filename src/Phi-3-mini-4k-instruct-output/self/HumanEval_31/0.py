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
    """
    # Step 1: Identify the characteristics of a prime number
    # Prime numbers are greater than 1
    # A prime number has no positive divisors other than 1 and itself

    # Step 2: Write a function to check if a given number 'n' is prime
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Step 3: For the main logic
# Start the loop from 2 and iterate up to (but not including) the square root of 'n'
# Use an efficient way to determine divisibility, such as the modulo operation
# Count and return the number of times 'n' is divisible (which should be 0 for prime numbers)