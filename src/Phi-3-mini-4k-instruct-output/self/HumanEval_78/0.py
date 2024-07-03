def is_hex_prime(digit):
    """Determine if a hexadecimal digit is prime.
    
    Args:
        digit (str): A single hexadecimal digit as a string.
        
    Returns:
        bool: True if the digit is prime, False otherwise.
    """
    hex_primes = {'2', '3', '5', '7', 'B', 'D'}
    return digit in hex_primes

def hex_key(num):
    """Count the number of hexadecimal digits that are primes.
    
    Args:
        num (str): A hexadecimal number as a string.
        
    Returns:
        int: The count of prime hexadecimal digits.
    """
    if not num:
        return 0
    
    # Count primes using list comprehension and the helper function
    prime_count = sum(is_hex_prime(digit) for digit in num)
    
    return prime_count