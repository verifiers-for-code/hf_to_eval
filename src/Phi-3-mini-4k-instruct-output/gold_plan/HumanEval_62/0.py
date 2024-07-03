def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]

    Action Plan:
    1. Initialize an empty result list to store the derivative coefficients.
    2. Iterate through the input list 'xs' using enumeration to get both index and value.
       - Start the enumeration from index 0, but we'll use (index + 1) as the multiplier.
    3. For each element (except the first one):
       - Multiply the coefficient by its corresponding power (index + 1).
       - Append this result to the result list.
    4. Return the result list containing the derivative coefficients.

    Note: Remember that the derivative of a constant (the first element) is always 0,
    so we don't include it in our result.
    """
    result = []
    for index, coeff in enumerate(xs):
        if index == 0:
            continue
        result.append(coeff * (index + 1))
    return result