import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    """
    # Check if the list has even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("List must have an even number of coefficients")

    # Find the largest non-zero coefficient
    largest_coeff = max(filter(lambda x: x != 0, xs), default=0)

    # Check if the largest non-zero coefficient is 0
    if largest_coeff == 0:
        raise ValueError("List must have at least one non-zero coefficient")

    # Find the degree of the polynomial
    degree = xs.index(largest_coeff)

    # Check if the degree is even
    if degree % 2 != 0:
        raise ValueError("The largest non-zero coefficient must be at an even index")

    # Find the zero point using the quadratic formula
    a = xs[degree]
    b = xs[degree - 1]
    c = 0

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is negative
    if discriminant < 0:
        raise ValueError("No real solutions")

    # Calculate the zero points
    zero1 = (-b + math.sqrt(discriminant)) / (2*a)
    zero2 = (-b - math.sqrt(discriminant)) / (2*a)

    # Return the zero point
    return zero1 if zero1 != zero2 else round(zero2, 2)