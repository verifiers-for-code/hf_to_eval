from typing import List


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
    1. Initialize an empty list to store the prime factors.
    2. Initialize a variable to the smallest prime number (2).
    3. While the input number is divisible by the current prime factor:
       a. Append the prime factor to the list.
       b. Divide the input number by the prime factor.
    4. Increment the prime factor by 1 and repeat step 3 until the input number is no longer divisible.
    5. If the remaining input number is greater than 1, append it to the list (it's a prime factor).
    6. Return the list of prime factors in the order from smallest to largest."""

    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors