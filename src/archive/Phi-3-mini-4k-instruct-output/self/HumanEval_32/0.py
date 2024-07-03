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
    # Step 1: Validate the input list
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    largest_non_zero_coeff = max(filter(lambda x: x != 0, xs), default=0)
    if largest_non_zero_coeff <= 0:
        raise ValueError("The largest non-zero coefficient must be positive and greater than zero.")
    
    # Step 2: Define a suitable range for iterating x
    x_range = [largest_non_zero_coeff]
    precision = 1e-6
    
    # Step 3: Use a numerical method to iteratively find the zero
    for x_guess in x_range:
        x = x_guess
        while abs(poly(xs, x)) > precision:
            # Step 4: Iterate and find the first zero
            f_x = poly(xs, x)
            f_prime_x = sum([coeff * i * math.pow(x, i-1) for i, coeff in enumerate(xs) if i > 0])
            x -= f_x / f_prime_x
        
        return round(x, 2)