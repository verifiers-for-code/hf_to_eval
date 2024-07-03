def simplify(x, n):
    """
    Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    

    Action Plan:
    1. Define a function `simplify` that takes two string parameters `x` and `n`.
    2. Parse the input fractions `x` and `n` into numerator and denominator using string manipulation.
    3. Calculate the product of the fractions by multiplying the numerators and denominators separately.
    4. Simplify the product by finding the greatest common divisor (GCD) of the numerator and denominator.
    5. Divide the numerator and denominator by the GCD to get the simplified product.
    6. Check if the simplified product is a whole number by comparing the numerator and denominator.
    7. Return `True` if the simplified product is a whole number, and `False` otherwise.
    
    Note: Use appropriate string manipulation and mathematical operations to implement the plan.
    Be careful when handling the GCD calculation and simplification process.
    """
    # Step 2: Parse the input fractions into numerator and denominator
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    # Step 3: Calculate the product of the fractions
    product_num = x_num * n_num
    product_denom = x_denom * n_denom

    # Step 4: Simplify the product by finding the GCD
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_val = gcd(product_num, product_denom)

    # Step 5: Divide the numerator and denominator by the GCD
    simplified_num = product_num // gcd_val
    simplified_denom = product_denom // gcd_val

    # Step 6: Check if the simplified product is a whole number
    return simplified_num == simplified_denom