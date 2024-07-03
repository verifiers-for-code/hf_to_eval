def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    """Return the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def largest_prime_digit_sum(lst):
    """Find the largest prime value and return the sum of its digits."""
    max_digit_sum = 0
    for num in lst:
        if is_prime(num):
            digit_sum = sum_of_digits(num)
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
    return max_digit_sum