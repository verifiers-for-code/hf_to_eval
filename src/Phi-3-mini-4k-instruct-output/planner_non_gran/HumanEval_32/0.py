import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    

    Action Plan:
    1. Define the polynomial evaluation function `poly` that takes a list of coefficients `xs` and a value `x` and returns the polynomial value at `x`.
    2. Implement the Newton-Raphson method for finding zeros:
        a. Initialize `x` with a reasonable starting value (e.g., 0).
        b. Calculate the derivative of the polynomial using the `poly` function.
        c. Iterate until convergence:
            - Calculate the next `x` value using the Newton-Raphson formula.
            - Check for convergence (e.g., absolute difference between `x` values is small).
            - Update `x` with the new value.
        d. Return the final `x` value as the zero of the polynomial.
    3. Handle edge cases:
        a. Ensure the input list `xs` has an even number of coefficients.
        b. Check if the largest non-zero coefficient is positive.
    4. Implement the `find_zero` function that takes a list of coefficients `xs` and returns the zero of the polynomial.
    5. Use the `find_zero` function to find the zero of a given polynomial.
    
    Note: Be careful with the implementation of the Newton-Raphson method and convergence criteria.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0 or xs[-1] <= 0:
        raise ValueError("Invalid input: xs must have an even number of coefficients and the largest non-zero coefficient must be positive.")
    
    x = 0
    epsilon = 1e-6
    max_iterations = 1000
    for _ in range(max_iterations):
        f_x = poly(xs, x)
        f_prime_x = poly(xs[:-1] + [0] * (len(xs) - 1), x)
        if abs(f_x) < epsilon:
            return x