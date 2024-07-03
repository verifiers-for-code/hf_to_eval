import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_sum_of_digits(lst):
    """Find the largest prime number in the list and return the sum of its digits."""
    largest_prime = 0
    for num in lst:
        if num > largest_prime and is_prime(num):
            largest_prime = num
    if largest_prime == 0:
        return 0
    else:
        return sum(int(digit) for digit in str(largest_prime))