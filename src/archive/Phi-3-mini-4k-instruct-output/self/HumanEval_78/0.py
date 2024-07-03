def is_hex_prime(digit):
    """Helper function to determine if a hexadecimal digit is prime."""
    hex_primes = {2, 3, 5, 7, 'B', 'D'}
    decimal_value = int(digit, 16)
    return decimal_value in hex_primes

def hex_key(num):
    """Counts the number of hexadecimal digits that are primes."""
    if not num:
        return 0
    
    return sum(is_hex_prime(digit) for digit in num)