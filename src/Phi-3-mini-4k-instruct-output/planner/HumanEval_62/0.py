def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    

    Action Plan:
    1. Initialize an empty list to store the coefficients of the derivative polynomial.
    2. Iterate through the input list of coefficients:
        a. For each coefficient, calculate the derivative by multiplying it by its corresponding power of x (which is the index of the coefficient in the list).
        b. Add the derivative to the list of coefficients.
    3. Return the list of coefficients as the derivative polynomial.
    
    Note: The derivative of a term ax^n is n*ax^(n-1).
    Be careful to handle the indexing correctly when calculating the derivative."""
    
    derivative_coeffs = []
    for i in range(len(xs)):
        derivative_coeffs.append(i * xs[i])
    return derivative_coeffs