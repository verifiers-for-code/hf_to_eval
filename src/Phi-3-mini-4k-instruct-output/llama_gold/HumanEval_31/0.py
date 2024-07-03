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
    1. Handle edge cases: if the input number (n) is less than 2, return False (not prime).
    2. Initialize a loop to check for divisors from 2 to n-1.
    3. Inside the loop, check if n is divisible by the current number (i.e., n % current_number == 0).
    4. If a divisor is found, return False (not prime).
    5. If the loop completes without finding a divisor, return True (prime)."""

    # Handle edge cases
    if n < 2:
        return False

    # Check for divisors
    for i in range(2, n):
        if n % i == 0:
            return False

    # If no divisors found, return True
    return True