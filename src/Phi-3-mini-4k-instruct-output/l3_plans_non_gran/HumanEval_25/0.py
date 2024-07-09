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
    1. Initialize an empty list to store the prime factors and a variable to store the current divisor.
    2. Start the divisor from 2, which is the smallest prime number.
    3. Implement a loop that continues until the input number `n` is fully factored.
    4. Inside the loop:
        a. Check if `n` is divisible by the current divisor.
        b. If `n` is divisible, divide `n` by the divisor and append the divisor to the list of prime factors.
        c. If `n` is not divisible, increment the divisor by 1.
    5. Once the loop exits, return the list of prime factors.
    6. Consider optimizing the divisor increment process to improve performance.
    
    Note: Ensure the implementation correctly handles the case where the input number is a prime number itself."""
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors