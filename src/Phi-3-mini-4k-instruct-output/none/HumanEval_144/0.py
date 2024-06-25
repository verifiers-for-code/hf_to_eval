from fractions import Fraction

def simplify(x, n):
    """
    Simplify the expression x * n, where x and n are string representations of fractions.
    The function returns True if x * n evaluates to a whole number and False otherwise.
    """
    # Convert the string fractions to Fraction objects
    x_frac = Fraction(x)
    n_frac = Fraction(n)

    # Multiply the fractions
    result = x_frac * n_frac

    # Check if the result is a whole number
    return result.denominator == 1