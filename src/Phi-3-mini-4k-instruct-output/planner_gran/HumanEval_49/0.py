def modp(n: int, p: int):
    """
    Return 2^n modulo p (be aware of numerics).
    
    Parameters:
    n (int): The exponent to raise 2 to.
    p (int): The modulus to take the modulo with.
    
    Returns:
    int: The result of 2^n modulo p.
    
    Examples:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    
    Action Plan:
    1. Define the function modp(n, p) with two integer parameters: n and p
    2. Handle the base case:
       - If n is 0, return 1 (since 2^0 = 1)
    3. Implement the recursive formula:
       - Calculate 2^(n - 1) modulo p using the modp function recursively
       - Multiply the result by 2
       - Take the modulus of the product with p (to ensure it stays within the range of p)
    4. Ensure correct handling of negative exponents:
       - Use the modp function recursively to calculate the result for n - 1
       - Multiply the result by 2 and take the modulus with p
    5. Optimize the calculation using modular arithmetic:
       - Use the modulus operator (%) to ensure the result stays within the range of p
       - This avoids overflow and ensures correct results for large exponents
    6. Return the final result:
       - The calculated result is 2^n modulo p
    
    Additional implementation details:
    - Consider using a docstring to provide a description of the function, its parameters, and its return value
    - Ensure the function handles edge cases, such as p = 0 or n < 0
    - Use appropriate variable names and comments to make the code readable and maintainable
    """
    if n == 0:
        return 1
    else:
        return (modp(n - 1, p) * 2) % p