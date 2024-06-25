
    def multiply(a, b):
        # Extract the unit digits of the input integers
        unit_digit_a = a % 10
        unit_digit_b = b % 10
        
        # Return the product of the unit digits
        return unit_digit_a * unit_digit_b