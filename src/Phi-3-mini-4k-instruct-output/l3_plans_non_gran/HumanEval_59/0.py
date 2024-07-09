def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    

    Action Plan:
    1. Define a function `largest_prime_factor` that takes an integer `n` as input, assuming `n > 1` and `n` is not a prime.
    2. Initialize a variable `factor` to 2, which is the smallest prime number.
    3. Loop until `factor` squared is less than or equal to `n`:
        a. Check if `n` is divisible by `factor` using the modulo operator (`n % factor == 0`).
        b. If `n` is divisible by `factor`, divide `n` by `factor` to reduce the search space.
        c. If `n` is not divisible by `factor`, increment `factor` by 1.
    4. After the loop, `factor` will be the largest prime factor of `n`.
    5. Return the `factor` as the largest prime factor of `n`.
    
    Note: Consider the case where `n` is a power of 2 (e.g., `n = 8`) and handle it accordingly."""
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return factor