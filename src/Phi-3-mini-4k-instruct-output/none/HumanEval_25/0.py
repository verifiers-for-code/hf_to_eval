from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    divisor = 2
    while n > 1:
        count = 0
        while n % divisor == 0:
            count += 1
            n //= divisor
        if count > 0:
            factors.append(divisor)
            factors.append(count)
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
                break
    return factors