def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Return True if the given number is the multiplication of 3 prime numbers, False otherwise."""
    if not isinstance(a, int) or a < 1 or a > 100:
        raise ValueError("Input must be an integer between 1 and 100.")
    
    if not is_prime(a):
        return False
    
    num = 2
    while a > 1:
        if a % num == 0:
            a //= num
            num += 1
            if num > 3:
                return False
        else:
            num += 1
    return True