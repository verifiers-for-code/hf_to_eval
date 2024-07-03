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

    Action Plan:
    1. Initialize the search interval:
       - Set 'begin' to -1.0 and 'end' to 1.0

    2. Expand the search interval:
       - While the polynomial values at 'begin' and 'end' have the same sign:
         - Double both 'begin' and 'end'
       This ensures the interval contains a zero crossing

    3. Implement the binary search:
       - While the difference between 'end' and 'begin' is greater than 1e-10:
         a. Calculate the midpoint 'center'
         b. Evaluate the polynomial at 'center'
         c. If the polynomial values at 'center' and 'begin' have the same sign:
            - Update 'begin' to 'center'
         d. Otherwise:
            - Update 'end' to 'center'

    4. Return the final value of 'begin' as the approximation of the zero point

    Note: Use the 'poly' function to evaluate the polynomial at different points.
    """
    if len(xs) % 2 != 0 or xs.count(0) > len(xs) // 2:
        raise ValueError("List of coefficients must have an even number of non-zero elements.")

    begin = -1.0
    end = 1.0

    while abs(end - begin) > 1e-10:
        if poly(xs, begin) * poly(xs, end) > 0:
            begin *= 2
            end *= 2
        else:
            center = (begin + end) / 2
            if poly(xs, center) * poly(xs, begin) > 0:
                begin = center
            else:
                end = center

    return begin