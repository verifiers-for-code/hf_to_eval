def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    

    Action Plan:
    1. Initialize an empty list to store the derivative coefficients.
    2. Check if the input list is empty:
        - If empty, return an empty list.
    3. Iterate through the input list, starting from the second element (index 1):
        - For each element, multiply it by the corresponding power of the input list length (i + 1).
        - Append the result to the derivative list.
    4. Return the derivative list, which represents the coefficients of the derivative polynomial.
    5. Note: The input list represents the coefficients of the original polynomial, and the derivative list represents the coefficients of the derivative polynomial."""
    
    derivative_coeffs = []
    if not xs:
        return derivative_coeffs
    
    for i in range(1, len(xs)):
        derivative_coeffs.append(xs[i] * (len(xs) - i))
    
    return derivative_coeffs