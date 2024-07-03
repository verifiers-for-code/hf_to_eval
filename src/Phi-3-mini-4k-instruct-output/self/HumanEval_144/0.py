from fractions import Fraction

def parse_fraction(fraction_str):
    """Parse a fraction string into numerator and denominator."""
    if not fraction_str:
        raise ValueError("Fraction string cannot be empty.")
    
    parts = fraction_str.split('/')
    if len(parts) != 2:
        raise ValueError("Fraction string must be in the format <numerator>/<denominator>.")
    
    numerator, denominator = parts
    if not numerator.isdigit() or not denominator.isdigit():
        raise ValueError("Both numerator and denominator must be positive whole numbers.")
    
    return int(numerator), int(denominator)

def simplify(x, n):
    """
    Simplify the expression x * n and return True if the result is a whole number, False otherwise.
    Both x and n are string representations of a fraction in the format <numerator>/<denominator>.
    """
    try:
        num_x, den_x = parse_fraction(x)
        num_n, den_n = parse_fraction(n)
    except ValueError as e:
        print(f"Error parsing fractions: {e}")
        return False
    
    # Multiply numerators and denominators
    result_num = num_x * num_n
    result_den = den_x * den_n
    
    # Check if the result is a whole number
    return result_den == 1