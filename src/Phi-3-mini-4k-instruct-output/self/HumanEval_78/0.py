def is_prime_hex_digit(digit):
    """Helper function to determine if a hexadecimal digit is prime."""
    hex_primes = {'2', '3', '5', '7', 'B', 'D'}
    return str(int(digit, 16)) in hex_primes

def hex_key(num):
    """Counts the number of hexadecimal digits that are primes."""
    if not num:
        return 0
    
    # Count primes using list comprehension
    prime_count = sum(is_prime_hex_digit(digit) for digit in num)
    
    return prime_count