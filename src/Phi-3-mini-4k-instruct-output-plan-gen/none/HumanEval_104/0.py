
def has_even_digit(num):
    """Check if a number has an even digit."""
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            return True
        num //= 10
    return False

def unique_digits(x):
    """Return a sorted list of all elements in x that don't have any even digits."""
    result = []
    for num in x:
        if not has_even_digit(num):
            result.append(num)
    return sorted(result)