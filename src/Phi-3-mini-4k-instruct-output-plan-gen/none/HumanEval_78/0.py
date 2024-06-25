
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are prime."""
    hex_digits = {'0': False, '1': False, '2': True, '3': True, '4': False,
                  '5': True, '6': False, '7': True, '8': False, '9': False,
                  'A': True, 'B': True, 'C': False, 'D': True, 'E': False, 'F': False}
    count = 0
    for char in num:
        if hex_digits[char]:
            count += 1
    return count