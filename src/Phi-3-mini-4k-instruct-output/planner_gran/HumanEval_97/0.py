def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    

    1. Extract the unit digits from the input numbers:
       - Use the modulo operator (%) to find the remainder of each number when divided by 10
       - This will give the unit digit of each number
    
    2. Multiply the unit digits:
       - Simply multiply the two extracted unit digits together
    
    3. Return the result:
       - The product of the unit digits is the result of the function
       - Return this value as an integer
    
    Additional implementation details:
    - Ensure the function handles valid integer inputs
    - The function does not need to handle error cases, as the problem statement assumes valid input
    - The function can be implemented in a single line of code, using the modulo operator and multiplication
    - The function should return an integer value"""
    return (a % 10) * (b % 10)