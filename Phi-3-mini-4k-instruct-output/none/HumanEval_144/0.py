
    from fractions import Fraction

    def simplify(x, n):
        """Your task is to implement a function that will simplify the expression
        x * n. The function returns True if x * n evaluates to a whole number and False
        otherwise. Both x and n, are string representation of a fraction, and have the following format,
        <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

        You can assume that x, and n are valid fractions, and do not have zero as denominator.

        simplify("1/5", "5/1") = True
        simplify("1/6", "2/1") = False
        simplify("7/10", "10/2") = False
        """

        # Convert the string fractions to Fraction objects
        x_frac = Fraction(x)
        n_frac = Fraction(n)

        # Multiply the fractions
        result = x_frac * n_frac

        # Check if the result is a whole number
        return result.denominator == 1