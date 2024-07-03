from typing import List
import math

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
    

    Action Plan:
    1. Implement a function to find prime factors for an input number:
        a. Initialize an empty list to store prime factors
        b. Loop from 2 to the square root of the number:
            i. If the number is divisible by the current loop value, add it to the prime factors list and divide the number by it
            ii. If it is not divisible, move to the next loop value
        c. If the number is greater than 2 after the loop, add the number itself as the last prime factor
    2. Check if the result list contains only one element (in which case, the original number is a prime and needs to be handled separately)
    3. Convert the prime factors list into a list of tuples, with each tuple holding a prime and its count
    4. Sort the list of tuples based on the prime factors in ascending order
    5. Flatten the list of tuples into a single list of prime factors
    6. Return the sorted list of prime factors
    7. Edge cases: Return an empty list for inputs like 1, negative numbers, and non-integers."""

    if not isinstance(n, int) or n <= 0:
        return []

    prime_factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 1:
        prime_factors.append(n)

    if len(prime_factors) == 1:
        return prime_factors

    prime_factors_with_count = [(prime, prime_factors.count(prime)) for prime in set(prime_factors)]
    prime_factors_with_count.sort()

    return [prime for prime, count in prime_factors_with_count for _ in range(count)]