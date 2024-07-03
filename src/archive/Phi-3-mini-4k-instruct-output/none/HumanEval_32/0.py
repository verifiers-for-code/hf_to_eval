import math
from typing import List


def poly(xs: List[float], x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: List[float]) -> float:
    """
    Finds x such that poly(x) = 0.
    find_zero returns only the zero point, even if there are many.
    It only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("List of coefficients must have even number of elements and largest non-zero coefficient.")
    
    # Find the largest non-zero coefficient
    largest_coeff = max(filter(lambda x: x != 0, xs))
    
    # Find the roots of the polynomial (x - largest_coeff) * poly(x) = 0
    # This is equivalent to finding the roots of the polynomial with coefficients [1, -largest_coeff]
    roots = [(-largest_coeff + math.sqrt(largest_coeff**2 - 4*1*0)) / 2,
             (-largest_coeff - math.sqrt(largest_coeff**2 - 4*1*0)) / 2]
    
    # Return the first root (since there might be multiple roots)
    return roots[0]