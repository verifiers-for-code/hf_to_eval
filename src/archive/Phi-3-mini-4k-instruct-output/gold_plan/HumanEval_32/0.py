import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xsx^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("The list of coefficients must have an even number of elements and the largest non-zero coefficient.")

    begin = -1.0
    end = 1.0

    while xs[-1] != 0:
        if poly(xs, begin) * poly(xs, end) > 0:
            end *= 2
        else:
            begin = (begin + end) / 2

    return round(begin, 2)