import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    
    Action Plan:
    1. Understand the problem:
        - The function find_zero takes a list of coefficients xs as input.
        - It returns the zero point of the polynomial represented by xs.
    
    2. Define the helper function poly:
        - This function evaluates the polynomial with coefficients xs at point x.
        - It uses the math.pow function to raise x to the power of i, where i is the index of the coefficient.
        - It returns the sum of the products of coefficients and x raised to the power of i.
    
    3. Define the find_zero function:
        - This function takes a list of coefficients xs as input.
        - It checks if the length of xs is even and the largest non-zero coefficient is positive.
        - If the conditions are met, it calls the root finding function find_zero_util.
    
    4. Implement the root finding algorithm:
        - Define the find_zero_util function.
        - It takes an initial guess x as input.
        - It calculates the value of the polynomial at x using the poly function.
        - It updates x based on the sign of the polynomial value and the derivative.
        - It returns the updated x.
    
    5. Handle edge cases:
        - Check for cases where the largest non-zero coefficient is not positive.
        - Handle cases where the polynomial has no real roots.
    
    Note: The plan assumes a basic understanding of numerical methods for root finding.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero_util(xs: list, x: float):
    """
    Finds the zero point of the polynomial represented by xs using the Newton-Raphson method.
    """
    while True:
        fx = poly(xs, x)
        if abs(fx) < 1e-6:
            return x
        dfx = poly(xs, 1)
        if dfx == 0:
            return None
        x -= fx / dfx


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0 or xs.count(0) > len(xs) // 2:
        return None
    if xs[-1] <= 0:
        return None
    return find_zero_util(xs, 0)