
    import math
    import cmath
    
    def poly(xs: list, x: float):
        """
        Evaluates polynomial with coefficients xs at point x.
        return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
        """
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    
    
    def find_zero(xs: list):
        """ xs are coefficients of a polynomial.
        find_zero find x such that poly(x) = 0.
        find_zero returns only zero point, even if there are many.
        Moreover, find_zero only takes list xs having even number of coefficients
        and largest non-zero coefficient as it guarantees a solution.
        """
        # Check if the list has even number of coefficients
        if len(xs) % 2 != 0:
            raise ValueError("List must have an even number of coefficients")
        
        # Check if the largest non-zero coefficient is non-zero
        if max(xs) == 0:
            raise ValueError("List must have a non-zero largest coefficient")
        
        # Find the largest non-zero coefficient
        largest_coeff = max(xs)
        
        # Find the index of the largest non-zero coefficient
        largest_coeff_index = xs.index(largest_coeff)
        
        # Calculate the derivative of the polynomial
        derivative_xs = [i * coeff for i, coeff in enumerate(xs)][1:]
        
        # Use the Newton-Raphson method to find the zero
        x0 = 1.0
        for _ in range(10):
            fx = poly(xs, x0)
            dfx = poly(derivative_xs, x0)
            if dfx == 0:
                break
            x0 = x0 - fx / dfx
        
        return round(x0, 2)