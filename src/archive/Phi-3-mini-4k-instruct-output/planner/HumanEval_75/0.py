import math

def is_prime(n):
    """Check if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Check if a number is the multiplication of 3 prime numbers.
    
    Args:
    a (int): The number to check.
    
    Returns:
    bool: True if the number is the multiplication of 3 prime numbers, False otherwise.
    """
    if a < 2 or a > 100:
        raise ValueError("Input must be between 2 and 100.")
    
    prime_count = 0
    for i in range(2, int(math.sqrt(a)) + 1):
        if is_prime(i) and a % i == 0:
            a //= i
            prime_count += 1
            if prime_count == 3:
                return True
    return False