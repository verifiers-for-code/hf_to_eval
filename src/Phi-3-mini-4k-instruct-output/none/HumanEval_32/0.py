import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0 or xs[0] == 0:
        raise ValueError("Invalid input: xs must have an even number of coefficients and the first coefficient must be non-zero.")

    # Find the largest non-zero coefficient
    largest_coeff = max(xs[1::2])

    # Find the index of the largest non-zero coefficient
    largest_coeff_index = xs[1::2].index(largest_coeff)

    # Calculate the zero point using the formula
    zero_point = largest_coeff_index - math.log(largest_coeff, xs[0])

    return round(zero_point, 2)