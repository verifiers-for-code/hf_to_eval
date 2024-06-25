def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Return True if the string length is a prime number, False otherwise"""
    length = len(string)
    return is_prime(length)