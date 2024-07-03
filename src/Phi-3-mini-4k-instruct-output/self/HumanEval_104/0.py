def has_even_digit(n):
    """Helper function to check if a number has even digits."""
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            return True
        n //= 10
    return False

def unique_digits(x):
    """Return a sorted list of all elements that haven't any even digit."""
    # Filter numbers without any even digits
    filtered_list = [num for num in x if not has_even_digit(num)]
    # Sort the filtered list
    sorted_list = sorted(filtered_list)
    return sorted_list