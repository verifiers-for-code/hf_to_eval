def modp(n: int, p: int) -> int:
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
    """
    # Input validation
    if not isinstance(n, int) or not isinstance(p, int):
        raise TypeError("Both n and p must be integers.")
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
    
    return result % p