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
    1. Parse the input fractions:
       a. Split each fraction string into numerator and denominator.
       b. Convert the split strings to integers.

    2. Calculate the product of the fractions:
       a. Multiply the numerators of x and n.
       b. Multiply the denominators of x and n.

    3. Check if the result is a whole number:
       a. Divide the product's numerator by its denominator.
       b. Check if the result is equal to its integer value.

    4. Return the result:
       a. If the result is a whole number, return True.
       b. Otherwise, return False.
    """
    # Step 1: Parse the input fractions
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    # Step 2: Calculate the product of the fractions
    product_num = x_num * n_num
    product_denom = x_denom * n_denom

    # Step 3: Check if the result is a whole number
    result = product_num / product_denom

    # Step 4: Return the result
    return result.is_integer()