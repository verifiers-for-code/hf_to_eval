def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
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
    1. Define the function modp with two parameters: n and p
    2. Calculate 2^n using the ** operator
    3. Handle potential overflow issues by using the modulo operator (%) to ensure the result is within the range of p
    4. Perform the modulo operation: (2^n) % p
    5. Return the result of the modulo operation
    
    Note: Be aware of potential overflow issues when calculating 2^n, especially for large values of n.
    Use the modulo operator to ensure the result is within the range of p."""
    return (2**n) % p