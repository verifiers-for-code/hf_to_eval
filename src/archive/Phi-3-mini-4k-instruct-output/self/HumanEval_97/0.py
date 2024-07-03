def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
    Action Plan:
    1. Set up the function definition taking two integer parameters, a and b.
    2. Extract unit digits of both numbers using modulo operation (i.e., number % 10)
    3. For handling negative numbers:
        a. If one or both numbers are negative, take the absolute value
        b. Maintain the original sign for the final product based on the sign of a and b
    4. Multiply the extracted digits (considering the sign of the final product)
    5. Return the result, ensuring that the sign of the product aligns with the sign of the inputs
    6. Test cases should include positive numbers, negative numbers, and one zero to validate edge cases
    """
    # Step 1: Set up the function definition
    def multiply(a, b):
        # Step 2: Extract unit digits
        digit_a = abs(a) % 10
        digit_b = abs(b) % 10
        
        # Step 3: Handle negative numbers
        sign = -1 if (a < 0) ^ (b < 0) else 1
        
        # Step 4: Multiply the extracted digits
        product = (digit_a * digit_b) * sign
        
        # Step 5: Return the result
        return product