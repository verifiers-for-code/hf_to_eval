
    def is_simple_power(x, n):
        """
        This function checks if a number x is a simple power of n.
        A number x is a simple power of n if n raised to the power of an integer equals x.
        
        :param x: The number to check
        :param n: The base number
        :return: True if x is a simple power of n, False otherwise
        """
        # Check if n is 1, as 1 raised to any power is always 1
        if n == 1:
            return x == 1
        
        # Check if x is 1, as 1 raised to any power is always 1
        if x == 1:
            return True
        
        # Check if n is 0 and x is not 0, as 0 raised to any power is 0
        if n == 0 and x != 0:
            return False
        
        # Check if n is negative and x is positive, as negative numbers cannot be simple powers
        if n < 0 and x > 0:
            return False
        
        # Check if n is 0 and x is negative, as 0 raised to any power is 0
        if n == 0 and x < 0:
            return False
        
        # Check if n is 1 and x is not 1, as 1 raised to any power is always 1
        if n == 1 and x != 1:
            return False
        
        # Check if n is 1 and x is 1, as 1 raised to any power is always 1
        if n == 1 and x == 1:
            return True
        
        # Check if n is 0 and x is not 0, as 0 raised to any power is 0
        if n == 0 and x != 0:
            return False
        
        # Check if n is negative and x is positive, as negative numbers cannot be simple powers
        if n < 0 and x > 0:
            return False
        
        # Check if n is 0 and x is negative, as 0 raised to any power is 0
        if n == 0 and x < 0:
            return False