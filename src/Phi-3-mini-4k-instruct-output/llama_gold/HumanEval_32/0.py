import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    

    Action Plan:
    1. Verify that the input list xs has an even number of coefficients and the largest non-zero coefficient as the last element.
    2. Initialize a range [begin, end] to search for the zero point, ensuring that poly(begin) and poly(end) have opposite signs.
    3. Expand the range exponentially until poly(begin) and poly(end) have opposite signs.
    4. Implement the bisection method:
       a. Calculate the midpoint center of the current range.
       b. Evaluate poly(center) and determine which half of the range to keep based on the sign of poly(center) and poly(begin).
       c. Update the range [begin, end] accordingly.
       d. Repeat steps a-c until the range is sufficiently small (e.g., end - begin < 1e-10).
    5. Return the approximate zero point as the current begin value."""
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Verify that the input list xs has an even number of coefficients and the largest non-zero coefficient as the last element.
    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("Input list xs must have an even number of coefficients and the largest non-zero coefficient as the last element.")
    
    # Initialize a range [begin, end] to search for the zero point, ensuring that poly(begin) and poly(end) have opposite signs.
    begin, end = -1000, 1000
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2
        end *= 2
    
    # Implement the bisection method.
    while end - begin > 1e-10:
        center = (begin + end) / 2
        if poly(xs, center) * poly(xs, begin) < 0:
            end = center
        else:
            begin = center
    
    # Return the approximate zero point as the current begin value.
    return begin