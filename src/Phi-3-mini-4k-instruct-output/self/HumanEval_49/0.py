def modp(n: int, p: int):
    """
    Return 2^n modulo p (be aware of numerics).
    
    Action Plan:
    1. Input validation:
        a. Check if both n and p are integers
        b. Verify n and p are non-negative
        c. Ensure p is greater than 1
    
    2. Special case handling:
        a. If n is zero, return 1 irrespective of the value of p, since any number to the power of zero is one.
        b. If p is one, return the value of n, as anything modulo one is itself.
    
    3. Applying modular exponentiation algorithm:
        a. Initialize the result to 1
        b. Iterate from 0 to n (inclusive):
            i. Update the result with: result = (result * base) mod p
            ii. Update the base with: base = (base * base) mod p
    
    4. Return the final result modulo p
    
    5. Edge cases:
        a. Large values of n and p should handle without overflow
        b. Negative values of n and p should be properly dealt with, potentially raising an exception or value error
    
    6. Testing:
        a. Verify all given test cases with additional edge cases for a comprehensive check
    """
    # Input validation
    if not isinstance(n, int) or not isinstance(p, int):
        raise ValueError("Both n and p must be integers.")
    if n < 0 or p < 0:
        raise ValueError("Both n and p must be non-negative.")
    if p <= 1:
        raise ValueError("p must be greater than 1.")
    
    # Special case handling
    if n == 0:
        return 1
    if p == 1:
        return n
    
    # Applying modular exponentiation algorithm
    result = 1
    base = 2
    for _ in range(n):
        result = (result * base) % p
        base = (base * base) % p
    
    return result