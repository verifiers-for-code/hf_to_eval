def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    

    Action Plan:
    1. Understand that the input list 'xs' represents coefficients of a polynomial, where xs[0] is the constant term, xs[1] is the coefficient of x, xs[2] is the coefficient of x^2, and so on.
    2. Initialize an empty list to store the coefficients of the derivative polynomial.
    3. Iterate through the input list, starting from the second element (index 1), since the derivative of the constant term is 0:
       a. For each element at index i, calculate its derivative as i * xs[i].
       b. Add this derivative to the result list.
    4. Return the resulting list, which represents the coefficients of the derivative polynomial."""

    result = []
    for i in range(1, len(xs)):
        result.append(i * xs[i])
    return result