def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Step 1
    derivative_coeffs = []

    # Step 2
    for i, coeff in enumerate(xs):
        # Step 3
        derivative_coeff = coeff * (i + 1)
        # Step 4
        derivative_coeffs.append(derivative_coeff)

    # Step 5
    return derivative_coeffs

# Step 6
if len(xs) < 2:
    return []