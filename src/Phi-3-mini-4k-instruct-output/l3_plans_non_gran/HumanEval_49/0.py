def modp(n: int, p: int):
    """
    Return 2^n modulo p (be aware of numerics).
    
    Action Plan:
    1. Define the function with two parameters: n and p
    2. Check if p is zero to avoid division by zero error
    3. If p is zero, return 1 (since any number modulo zero is 1)
    4. Use the modulo operator (%) to perform the modulo operation: 2^n % p
    5. Return the result of the modulo operation
    6. Consider adding input validation for n and p (e.g., ensuring they are integers)
    """
    # Input validation
    if not isinstance(n, int) or not isinstance(p, int):
        raise ValueError("Both n and p must be integers.")
    
    # Check if p is zero to avoid division by zero error
    if p == 0:
        return 1
    
    # Calculate 2^n modulo p
    result = pow(2, n, p)
    
    return result