import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds x such that poly(x) = 0.
    Returns only the zero point, even if there are many.
    Only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    """
    # Step 1: Initialize the search interval
    begin = -1.0
    end = 1.0

    # Step 2: Expand the search interval
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2
        end *= 2

    # Step 3: Implement the binary search
    while end - begin > 1e-10:
        center = (begin + end) / 2
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center

    # Step 4: Return the final value of 'begin' as the approximation of the zero point
    return round(begin, 2)