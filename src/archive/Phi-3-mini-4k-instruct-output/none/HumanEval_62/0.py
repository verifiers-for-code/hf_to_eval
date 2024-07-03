def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Create a new list to store the derivative coefficients
    derivative_xs = []
    
    # Iterate through the input list
    for i in range(1, len(xs)):
        # Calculate the derivative coefficient and append it to the new list
        derivative_xs.append(i * xs[i])
    
    return derivative_xs