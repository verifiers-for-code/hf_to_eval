import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    

    Action Plan:
    1. Validate the input list:
        a. Check if the length of `xs` is even
        b. Ensure the largest non-zero coefficient is positive and greater than zero
    
    2. Define a suitable range for iterating `x` based on the largest non-zero coefficient:
        a. Start the range from the largest non-zero coefficient
        b. Consider the size and nature of `xs` to determine the precision level needed
    
    3. Use a numerical method to iteratively find the zero:
        a. Implement the Newton-Raphson method or another suitable optimization technique
        b. Utilize the `poly` function within the optimization method
    
    4. Iterate and find the first zero:
        a. Start from the largest non-zero coefficient and use a small initial guess
        b. Evaluate `poly(x)` at the current guess
        c. Adjust the guess using the derivative of the polynomial and the function's value
        d. Continue until the function value is approximately zero
    
    5. Handle exceptions and edge cases:
        a. Provide feedback if the function does not converge or if the largest non-zero coefficient is zero
    
    6. Return the found zero or indicate no zero found:
        a. Return the found zero if convergence is achieved within the specified range
        b. If no zero is found, return a message or default value"""
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    
    largest_coeff = max(xs)
    if largest_coeff <= 0:
        raise ValueError("The largest non-zero coefficient must be positive and greater than zero.")
    
    # Define a suitable range for iterating x based on the largest non-zero coefficient
    # Here, we use a simple approach of starting from the largest non-zero coefficient
    # and using a small initial guess. The precision level can be adjusted based on the size and nature of xs.
    x = largest_coeff
    precision = 1e-6
    
    # Implement the Newton-Raphson method to iteratively find the zero
    # We use the derivative of the polynomial to adjust the guess
    # The iteration stops when the function value is approximately zero
    for i in range(100):
        f_x = poly(xs, x)
        if abs(f_x) < precision:
            return x
        
        # Calculate the derivative of the polynomial
        derivative = sum([coeff * (i + 1) * math.pow(x, i) for i, coeff in enumerate(xs)])
        
        # Adjust the guess using the derivative and the function's value
        x -= f_x / derivative
    
    # Handle exceptions and edge cases
    # If the function does not converge or if the largest non-zero coefficient is zero,
    # provide feedback and return a default value