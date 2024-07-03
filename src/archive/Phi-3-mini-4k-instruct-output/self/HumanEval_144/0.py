from fractions import Fraction

def parse_fraction(fraction_str):
    """Helper function to parse the string fraction into a numerator and denominator."""
    if not fraction_str:
        raise ValueError("Empty string input")
    
    parts = fraction_str.split('/')
    if len(parts) != 2:
        raise ValueError("Invalid fraction format")
    
    numerator, denominator = int(parts[0]), int(parts[1])
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    return numerator, denominator

def simplify(x, n):
    """Function to simplify the expression x * n. Returns True if x * n evaluates to a whole number, False otherwise."""
    try:
        x_num, x_denom = parse_fraction(x)
        n_num, n_denom = parse_fraction(n)
    except ValueError as e:
        print(f"Error: {e}")
        return False
    
    product_num = x_num * n_num
    product_denom = x_denom * n_denom
    
    # Check if the result is a whole number
    if product_denom == 1:
        return True
    else:
        return False