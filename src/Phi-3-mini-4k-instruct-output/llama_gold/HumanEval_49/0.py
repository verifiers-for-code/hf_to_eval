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
    1. Understand that the function calculates 2^n modulo p, where n and p are integers.
    2. Initialize a variable (e.g., ret) to store the result, setting it to 1 (the multiplicative identity).
    3. Iterate n times to calculate 2^n:
       a. In each iteration, multiply the current result by 2.
       b. Immediately apply the modulo operation with p to the result.
    4. After the iterations, return the final result."""
    
    ret = 1
    for _ in range(n):
        ret = (ret * 2) % p
    return ret