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
    1. Extract the unit digit of 'a':
       - Use the modulo operator (%) with 10 to get the remainder
       - This will give you the unit digit of 'a'

    2. Extract the unit digit of 'b':
       - Use the same method as step 1, but for 'b'

    3. Handle negative numbers:
       - Consider using the absolute value function to ensure
         positive unit digits

    4. Multiply the extracted unit digits:
       - Perform the multiplication of the two unit digits

    5. Return the result:
       - The product of the unit digits is the final result

    Implement the function following these steps to solve the problem.
    """
    # Extract the unit digit of 'a'
    unit_digit_a = abs(a) % 10

    # Extract the unit digit of 'b'
    unit_digit_b = abs(b) % 10

    # Multiply the extracted unit digits
    product = unit_digit_a * unit_digit_b

    # Return the result
    return product