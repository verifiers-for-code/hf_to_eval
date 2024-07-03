def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    

    1. Understand the input:
       - The input is a list of coefficients, where xs[0] is the constant term, xs[1] is the coefficient of x, xs[2] is the coefficient of x^2, and so on.
    
    2. Calculate the derivative:
       - Initialize an empty list to store the coefficients of the derivative polynomial
       - Iterate over the input list of coefficients:
         a. For each coefficient, calculate the derivative using the power rule (coefficient * power)
         b. Decrement the power by 1
         c. Append the calculated coefficient to the result list
    
    3. Return the result:
       - Return the list of coefficients representing the derivative polynomial
    
    Additional implementation details:
    - Use a loop or list comprehension to iterate over the input list of coefficients
    - Use the power rule to calculate the derivative of each term (coefficient * power)
    - Decrement the power by 1 for each term
    - Ensure the function handles edge cases, such as an empty input list or a list with a single coefficient
    - Consider using a more efficient approach, such as using the `enumerate` function to iterate over the input list with indices"""
    if not xs:
        return []
    result = []
    for i, coeff in enumerate(xs[1:], start=1):
        result.append(coeff * i)
    return result