from typing import List
import math

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    
    Action Plan:
    1. Initialize an empty list to store prime factors.
    2. Start with the smallest prime number (2) as the initial divisor.
    3. While the divisor is less than or equal to the square root of n:
       a. If n is divisible by the current divisor:
          - Add the divisor to the list of factors.
          - Divide n by the divisor.
          - Do not increment the divisor (to catch repeated factors).
       b. If n is not divisible by the current divisor:
          - Increment the divisor.
    4. After the loop, if n is greater than 1, it is a prime factor itself:
       - Add n to the list of factors.
    5. Return the list of prime factors.

    Note: Using the square root of n as the upper bound for the divisor 
    search optimizes the algorithm, as any factor larger than √n would 
    have a corresponding factor smaller than √n.
    """
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    if n > 1:
        factors.append(n)
    return factors