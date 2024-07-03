from fractions import Fraction

def parse_fraction(fraction_str):
    """
    Helper function to parse a string fraction into numerator and denominator.
    Handles edge cases like empty strings or incorrect format.
    """
    if not fraction_str:
        raise ValueError("Empty string input")
    parts = fraction_str.split('/')
    if len(parts) != 2:
        raise ValueError("Invalid fraction format")
    numerator, denominator = parts
    if not numerator.isdigit() or not denominator.isdigit():
        raise ValueError("Non-numeric values in fraction")
    return int(numerator), int(denominator)

def simplify(x, n):
    """
    Function to simplify the expression x * n. Returns True if x * n evaluates to a whole number, False otherwise.
    Both x and n are string representations of a fraction in the format <numerator>/<denominator>.
    """
    try:
        numerator_x, denominator_x = parse_fraction(x)
        numerator_n, denominator_n = parse_fraction(n)
    except ValueError as e:
        print(f"Error: {e}")
        return False

    # Perform the multiplication of the numerators and denominators separately
    numerator_result = numerator_x * numerator_n
    denominator_result = denominator_x * denominator_n

    # Check if the result (numerator/denominator) is a whole number by verifying if the denominator is 1
    return denominator_result == 1