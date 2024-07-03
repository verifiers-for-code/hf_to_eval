def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    

    Action Plan:
    1. Split each input string into numerator and denominator using the '/' character as a separator.
    2. Convert the extracted numerators and denominators into integers.
    3. Calculate the product of the two fractions by multiplying their numerators and denominators separately.
    4. Check if the result of the division of the product's numerator by its denominator is a whole number.
       a. Perform the division and check if the result is equal to its integer value.
       b. If it is, return True, indicating the product is a whole number.
       c. Otherwise, return False."""

    # Step 1: Split each input string into numerator and denominator
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    # Step 2: Calculate the product of the two fractions
    product_num = x_num * n_num
    product_denom = x_denom * n_denom

    # Step 3: Check if the result of the division of the product's numerator by its denominator is a whole number
    if product_num % product_denom == 0:
        return True
    else:
        return False