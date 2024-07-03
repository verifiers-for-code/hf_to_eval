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
    """
    # Step 1: Implement a function to find prime factors for an input number
    prime_factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 2:
        prime_factors.append(n)

    # Step 2: Check if the result list contains only one element (in which case, the original number is a prime and needs to be handled separately)
    if len(prime_factors) == 1:
        return [prime_factors[0]]

    # Step 3: Convert the prime factors list into a list of tuples, with each tuple holding a prime and its count
    prime_factors_with_count = [(prime, prime_factors.count(prime)) for prime in set(prime_factors)]

    # Step 4: Sort the list of tuples based on the prime factors in ascending order
    prime_factors_with_count.sort(key=lambda x: x[0])

    # Step 5: Flatten the list of tuples into a single list of prime factors
    result = [prime for prime, count in prime_factors_with_count for _ in range(count)]

    # Step 6: Return the sorted list of prime factors
    return result