import math


def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): List of coefficients of the polynomial.
    x (float): The point at which to evaluate the polynomial.
    
    Returns:
    float: The value of the polynomial at x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def derivative(xs: list) -> list:
    """
    Calculates the derivative of the polynomial with coefficients xs.
    
    Args:
    xs (list): List of coefficients of the polynomial.
    
    Returns:
    list: List of coefficients of the derivative polynomial.
    """
    return [i * coeff for i, coeff in enumerate(xs)][1:]


def newton_raphson(xs: list, x: float, tolerance: float = 1e-7) -> float:
    """
    Finds the zero of the polynomial with coefficients xs using the Newton-Raphson method.
    
    Args:
    xs (list): List of coefficients of the polynomial.
    x (float): Initial guess for the zero of the polynomial.
    tolerance (float): The convergence criterion.
    
    Returns:
    float: The zero of the polynomial.
    """
    while True:
        fx = poly(xs, x)
        dfx = poly(derivative(xs), x)
        
        if abs(fx) < tolerance:
            return x
        
        x = x - fx / dfx


def find_zero(xs: list) -> float:
    """
    Finds the zero of the polynomial with coefficients xs.
    
    Args:
    xs (list): List of coefficients of the polynomial.
    
    Returns:
    float: The zero of the polynomial.
    
    Raises:
    ValueError: If the list of coefficients does not have an even number of elements or the largest non-zero coefficient is not positive.
    """
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    
    if xs[-1] <= 0:
        raise ValueError("The largest non-zero coefficient must be positive.")
    
    return newton_raphson(xs, 0)